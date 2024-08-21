from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from django.db import models
from django.db.models import Avg 
from .models import UploadedImage, PerformanceData


def UploadButton(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = UploadedImage(image=request.FILES['image'])  # Handle the image
            uploaded_image.save()
            return redirect('result', image_id=uploaded_image.id)
    else:
        form = ImageUploadForm()
    return render(request, 'Website/upload_button.html', {'form': form})

def MyImages(request):
    return render(request, 'Website/my_images.html')

from django.http import HttpResponse
from django.conf import settings
import os

def download_original(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'original_image.jpg')
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="image/jpeg")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response

def download_segmented(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'segmented_image.jpg')
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="image/jpeg")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response

def performance_metrics(request):
    # Get the average processing time and accuracy from your data source
    average_processing_time = 0.45  # Replace with your actual value
    average_accuracy = 98.5  # Replace with your actual value

    context = {
        'processing_time': average_processing_time,
        'accuracy': average_accuracy,
    }
    return render(request, 'Website/performance.html', context)




def FeedbackPage(request):
    if request.method == 'POST':
        feed_back = request.POST.get('feedback')
        # Here you would typically save the feedback to a database or handle it as needed
        return HttpResponse("Thank you for your feedback!")

    return render(request, 'Website/feedback.html')
