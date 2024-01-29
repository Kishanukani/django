from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path("",include())
    path("", include("Resume.urls")),
    path("admin/", admin.site.urls),
]
