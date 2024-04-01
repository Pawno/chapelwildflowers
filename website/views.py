import pdb
import re, os
import sys
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import EmailSubscriber
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.

EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"


@csrf_exempt
def subscribe(request):
    # TODO add a rate limiter on this endpoint
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            if re.match(EMAIL_REGEX, email):
                EmailSubscriber.objects.get_or_create(email=email)
                return JsonResponse(
                    {"message": "Thank you for subscribing!"}, status=201
                )
            else:
                return JsonResponse({"error": "Email is invalid."}, status=400)
        else:
            return JsonResponse(
                {"error": "Email is required.", "post": request.POST}, status=400
            )
    else:
        return JsonResponse({"error": "Invalid request."}, status=400)


@csrf_exempt
def imageSubmissions(request):
    # TODO add a rate limiter on this endpoint
    print("REQUESTREQUESTREQUESTREQUEST REQUESTREQUESTREQUEST")
    if request.method == "POST" and request.FILES.getlist("fileInput"):
        files = request.FILES.getlist("fileInput")
        if files[0]:
            fs = FileSystemStorage(
                location=os.path.join(settings.MEDIA_ROOT, "for_review")
            )
            for file in files:
                fs.save(file.name, file)
            return JsonResponse({"message": "Files uploaded successfully"}, status=201)
        else:
            return JsonResponse({"error": "No files."}, status=400)
    else:
        return JsonResponse({"error": "Invalid request."}, status=400)
