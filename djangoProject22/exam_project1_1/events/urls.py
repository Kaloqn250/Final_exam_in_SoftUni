from django.urls import path

from exam_project1_1.events import views

urlpatterns = [
    path('details/<int:pk>', views.EventDetailView.as_view(), name='event_details'),
    path('events/', views.EventListView.as_view(), name='event_list'),
    path('register/', views.EventCreateView.as_view(), name='event_create'),
    path('delete/<int:pk>', views.EventDeleteView.as_view(), name='event_delete'),
    path('edit/<int:pk>', views.EventEditView.as_view(), name='event_edit'),
]