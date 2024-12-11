from django.urls import path

from exam_project1_1.feedback import views

urlpatterns = [
    path('create_feedback/<int:pk>', views.CreateFeedbackView.as_view(), name='create_feedback'),
    path('delete_feedback/<int:pk>', views.DeleteFeedbackView.as_view(), name='delete_feedback'),
    path('edit_feedback/<int:pk>', views.EditFeedbackView.as_view(), name='edit_feedback'),
]