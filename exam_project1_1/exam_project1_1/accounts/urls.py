from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from exam_project1_1.accounts import views

urlpatterns = [
    path('register/', views.CreateProfileView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('details/', views.ProfileDetailView.as_view(), name='details'),
]