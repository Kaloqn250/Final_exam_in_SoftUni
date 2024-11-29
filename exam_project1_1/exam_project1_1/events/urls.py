from django.urls import path

from exam_project1_1.events import views

urlpatterns = [
    path('details/<int:pk>', views.EventDetailView.as_view(), name='details'),
    path('events/', views.EventListView.as_view(), name='event_list'),
    path('register/', views.EventCreateView.as_view(), name='event_create'),
]