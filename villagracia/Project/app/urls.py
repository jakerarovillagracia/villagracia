from django.urls import path
from .views import  HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), 'home'),
    path('about', AboutPageView.as_view(), 'about'),
]