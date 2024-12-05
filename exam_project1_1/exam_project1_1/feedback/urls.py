from django.urls import path

from exam_project1_1.feedback import views

urlpatterns = [
    path('create_feedback/<int:pk>', views.CreateFeedbackView.as_view(), name='create_feedback'),
    path('details/<int:pk>', views.FeedbackDetailsView.as_view(), name='feedback_details'),
]