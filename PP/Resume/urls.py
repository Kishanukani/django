from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome),
    path("resume/", views.Resume, name="resume"),
    path("sign_up/", views.Signup, name="sign_up"),
]
