from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import firebase_admin
from firebase_admin import credentials, storage
from datetime import timedelta


def welcome(request):
    return render(request, "index.html")


def index(request):
    return render(request, "index.html")


def resumepage(request):
    return render(request, "Resume.html")


def Signup(request):
    return render(request, "sign_up.html")


def upload_resume(request):
    if request.method == "POST" and request.FILES["uploadresume"]:
        upload_resume = request.FILES["uploadresume"]

        # Initialize Firebase Admin SDK
        cred = credentials.Certificate(settings.FIREBASE_SERVICE_ACCOUNT_KEY_PATH)
        # firebase_admin.initialize_app(
        #     cred,
        #     name="ResumeApp",
        #     options={"storageBucket": settings.FIREBASE_STORAGE_BUCKET},
        # )
        bucket = storage.bucket(settings.FIREBASE_STORAGE_BUCKET)

        # Store user's resume in Firebase Storage
        filename = upload_resume.name
        blob = bucket.blob(f"userresume/{filename}")
        blob.upload_from_file(upload_resume)

        context = {"resume_uploaded": True}
    else:
        context = {"resume_uploaded": False}

    return render(request, "upload_resume.html", context)


# Create your views here.
