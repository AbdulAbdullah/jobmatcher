import mimetypes
from rest_framework import serializers
from .models import Resume, JobPosting, Match

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['file']

    def validate_file(self, value):
        detected_type, _ = mimetypes.guess_type(value.name)
        allowed_types = [
            'application/pdf',
            'application/msword',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        ]

        if detected_type not in allowed_types:
            raise serializers.ValidationError("Unsupported file type.")
        if value.size > 5 * 1024 * 1024:  # 5 MB limit
            raise serializers.ValidationError("File size exceeds the 5MB limit.")
        return value

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
