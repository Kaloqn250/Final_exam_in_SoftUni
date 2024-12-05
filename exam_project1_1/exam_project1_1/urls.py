from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('exam_project1_1.events.urls')),
    path('', include('exam_project1_1.common.urls')),
    path('accounts/', include('exam_project1_1.accounts.urls')),
    path('feedbacks/', include('exam_project1_1.feedback.urls')),
    path('bookings/', include('exam_project1_1.booking.urls')),
    path('categories/', include('exam_project1_1.category.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)