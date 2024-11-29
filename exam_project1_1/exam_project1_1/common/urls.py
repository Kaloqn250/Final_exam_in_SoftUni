from django.urls import path

from exam_project1_1.common import views

urlpatterns = [
    path('', views.home, name='home'),
]
