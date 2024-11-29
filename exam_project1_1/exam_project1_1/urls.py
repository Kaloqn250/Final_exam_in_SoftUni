from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('exam_project1_1.events.urls')),
    path('', include('exam_project1_1.common.urls')),
    path('accounts/', include('exam_project1_1.accounts.urls')),
]
