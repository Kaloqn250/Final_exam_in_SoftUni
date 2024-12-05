from django.urls import path

from exam_project1_1.category import views

urlpatterns = [
    path('create_category/', views.CreateCategoryView.as_view(), name='create_category'),
]