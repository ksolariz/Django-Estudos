from django.urls import path, include

from . import views

urlpatterns = [
    path("<int:month>", views.monthly_challenge_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
    
]
