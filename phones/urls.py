from django.urls import path
from .views import *


urlpatterns = [
    path(
        "",
        home,
        name="home"
    ),
    path(
        "phones/<int:pk>/", 
        phone_details,
        name="details"
    ),   
]