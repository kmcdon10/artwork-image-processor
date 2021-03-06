# settings import not used at this time
#from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from artwork_image_processor.models import Image
from artwork_image_processor.forms import ImageForm

from artwork_image_processor.style import run_style_transfer

# Create your views here.

# Primary Page (Image Upload, Processing, etc)
def home(request):
    if request.method == 'POST':
        imageForm = ImageForm(request.POST, request.FILES)
        if imageForm.is_valid():
           
            # the uploaded image is passed to the style transfer method
            uploadedImage = imageForm.save()
            styledImage = run_style_transfer(uploadedImage)
             
            content = {
                'imageForm': imageForm,
                'image': styledImage, 
            }
            return render(request, 'home.html', content)
    else:
        imageForm = ImageForm() 
    return render(request, 'home.html', {
        'imageForm': imageForm,  
    })

def about(request):
    print("--- Render: ABOUT ---")
    content = {}
    return render(request, 'about.html', content)

# result transformed image result page
def image(request):
    return render(request, 'image.html', {'image': image })

def images(request):
    images = Image.objects.all()
    return render(request, 'image-list.html', { 'images': images })

# not currently being used
def index(request):
    return HttpResponse("Hello, world. You're at the aip index.")
