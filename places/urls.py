from places.views import ParkView, CountryParkView
from django.urls import path

app_label = 'places'
urlpatterns = [
    path('park/<int:pk>/', ParkView.as_view()),
    path('country/<int:pk>/top/', CountryParkView.as_view())
]
