from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from .filehandler import handle_uploaded_file
from .models import Image

from .functions import detect
from .functions import generate_images, generate_images_path, get_stored_dir

import os, shutil

app_name = 'explorer'

# Create your views here.
def find_images(request):
    if request.method == 'POST':
        keywords = request.POST.get('keywords').replace(' ','_')
        assert keywords
        img_count = int(request.POST.get('count'))
        assert img_count
        dic=[keywords,img_count]
        stored_dir = get_stored_dir(keywords)
        generate_images(keywords,img_count,stored_dir, generate_images_path)
        path = generate_images_path
        shutil.make_archive(keywords, 'zip', path)
        new_path = os.path.join(os.getcwd(),keywords)
        zip_path = f'{new_path}.zip'
        return render(request, 'explorer/find_images.html', {
        'dic':dic,
        'path':zip_path,
        })
    return render(request, 'explorer/find_images.html', {
        
    })

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

from PIL import Image as im

def detection(request):
    django_img_path = None

    if request.method == 'POST':
        image = request.FILES['image']
        img_name = image.name

        image = im.open(image)
        parent_path = os.path.abspath('media') 
        images_path = os.path.join(parent_path,'images')
        img_path = f'{images_path}/{img_name}'
        image.save(img_path)

        returned_image = detect(img_path, is_path=True) #ndarray
        returned_image = im.fromarray(returned_image) #convert to image

        assert os.path.exists(img_path)
        
        returned_image.save(img_path)
        django_img_path = f'/media/images/{img_name}'

    return render(request, "explorer/detection.html", {
        'img_path':django_img_path
    })

def train(request):
    return render(request, 'explorer/train.html', {})

def About(request):
    return render(request, 'explorer/About.html', {})

def What_is_AI(request):
    return render(request, 'explorer/What_is_AI.html', {})

def Steps(request):
    return render(request, 'explorer/Steps.html', {})

def Home(request):
    return render(request, 'explorer/Home.html', {})

def Contact(request):
    return render(request, 'explorer/Contact.html', {})