from django.urls import path, include
from .views import HomeView, RegisterView

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('', HomeView.as_view(), name="home"),
    path('register', RegisterView.as_view(), name="register"),
]