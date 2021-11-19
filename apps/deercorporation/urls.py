from django.urls import path

from apps.deercorporation.views import RideHistroyView

app_name = "deercorporation"

urlpatterns = [
    path("<int:pk>/", RideHistroyView.as_view()),
]
