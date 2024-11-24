from django.db import models

class Resume(models.Model):
    candidate_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.candidate_name


class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    required_skills = models.TextField()

    def __str__(self):
        return self.title


class Match(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    match_score = models.FloatField()

    def __str__(self):
        return f"{self.resume.candidate_name} - {self.job_posting.title}"
