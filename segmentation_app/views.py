from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import UploadedImage


def home(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = UploadedImage(image=request.FILES['image'])  # Handle the image
            uploaded_image.save()
            return redirect('result', image_id=uploaded_image.id)
    else:
        form = ImageUploadForm()
    return render(request, 'segmentation_app/home.html', {'form': form})