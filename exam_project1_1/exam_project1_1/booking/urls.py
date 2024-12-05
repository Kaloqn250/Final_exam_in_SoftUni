from django.urls import path

from exam_project1_1.booking import views

urlpatterns = [
    path('book_event/<int:pk>   ', views.BookEventView.as_view(), name='book_event'),
]