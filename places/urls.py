from places.views import ParkView
from django.urls import path

app_label = 'places'
urlpatterns = [
    path('park/<int:pk>/', ParkView.as_view()),
]
