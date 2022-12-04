from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from .filehandler import handle_uploaded_file
from .models import Image

from .functions import detect

import os

app_name = 'explorer'

photos = []

# Create your views here.
def upload(request):
    ##Process images uploaded by users###
    # if request.method == 'POST':
    #     form = ImageForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         # Get the current instance object to display in the template
    #         img_obj = form.instance
    #         return render(request, 'explorer/upload.html', {
    #             'form': form,
    #             'img_obj': img_obj
    #             })

    # return render(request, 'explorer/upload.html', {
    #     'form': ImageForm()
    #     })
    all_images = []
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            # form = ImageForm('None',image)
            # print(form.is_valid())
            # form.save()
            # images.append(form.instance)
            try: 
                img_obj = Image.objects.create(title='none',image=image)
                all_images.append(img_obj)
            except: pass

    return render(request, 'explorer/upload.html', {
        'images': all_images})

def show(request):
    if request.method == 'POST':
        remove_all_images()
    images = Image.objects.all()
    return render(request,"explorer/show.html",{
        'images':images,
    })

def remove_all_images():
    Image.objects.all().delete()
    parent_path = os.path.abspath('media') 
    images_path = os.path.join(parent_path,'images')   
    all_images = os.listdir(images_path)
    for image in all_images:
        image_path = os.path.join(images_path,image)
        os.remove(image_path)

def detection(request):
    detect('sheep.jpg')
    return render(request, "explorer/detection.html", {

    })
