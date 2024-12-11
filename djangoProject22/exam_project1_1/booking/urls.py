from django.urls import path

from exam_project1_1.booking import views

urlpatterns = [
    path('book_event/<int:pk>   ', views.BookEventView.as_view(), name='book_event'),
    path('booking_details/<int:pk>', views.BookingDetailsView.as_view(), name='booking_details'),
    path('cancel_booking/<int:pk>', views.DeleteBooking.as_view(), name='cancel_booking')
]