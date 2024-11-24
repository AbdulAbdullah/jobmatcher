from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Resume, JobPosting, Match
from .services import extract_text_from_resume, extract_skills, calculate_match_score
from .serializers import ResumeSerializer, JobPostingSerializer, MatchSerializer

class ResumeUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        print(request.data) 
        print("Files:", request.FILES)
        print("Headers:", request.headers)
        serializer = ResumeSerializer(data={'file': request.FILES.get('file')})

        if serializer.is_valid():
            try:
                resume = serializer.save()
                extracted_text = extract_text_from_resume(resume.file)
                skills = extract_skills(extracted_text)
                return Response({
                    "message": "Resume uploaded successfully",
                    "skills": list(skills)
                }, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        print("Serializer Errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobPostingView(APIView):
    def post(self, request):
        serializer = JobPostingSerializer(data=request.data)
        if serializer.is_valid():
            job_posting = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobPostingListView(APIView):
    def get(self, request):
        job_postings = JobPosting.objects.all()
        serializer = JobPostingSerializer(job_postings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class JobMatchView(APIView):
    def post(self, request):
        resume_id = request.data.get("resume_id")
        job_id = request.data.get("job_id")

        if not resume_id or not job_id:
            return Response({"error": "Both resume_id and job_id are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            resume = Resume.objects.get(id=resume_id)
        except Resume.DoesNotExist:
            return Response({"error": "Resume not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            job = JobPosting.objects.get(id=job_id)
        except JobPosting.DoesNotExist:
            return Response({"error": "Job posting not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            match_score = calculate_match_score(resume, job)
            match, created = Match.objects.get_or_create(resume=resume, job_posting=job, defaults={"match_score": match_score})
            if not created:
                match.match_score = match_score  # Update match score if already exists
                match.save()
            serializer = MatchSerializer(match)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
