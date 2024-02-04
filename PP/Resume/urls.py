from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.welcome),
    path("resumepage/", views.resumepage, name="resumepage"),
    path("index", views.index, name="index"),
    path("sign_up/", views.Signup, name="sign_up"),
    path(
        "upload_resume/", views.upload_resume, name="upload_resume"
    ),  # Use a different URL pattern for upload_resume
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
