from django.urls import path
from .views import ResumeUploadView, JobMatchView, JobPostingView, JobPostingListView

urlpatterns = [
    path('upload-resume/', ResumeUploadView.as_view(), name='upload_resume'),
    path('match-job/', JobMatchView.as_view(), name='match_job'),
    path('post-job/', JobPostingView.as_view(), name='job_postings'),
    path('job-postings/<int:pk>/', JobPostingView.as_view(), name='job_posting_detail'),
    path('job-postings/', JobPostingListView.as_view(), name='job_posting_list'),
]
