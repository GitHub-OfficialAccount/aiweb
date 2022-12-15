from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from .filehandler import handle_uploaded_file
from .models import Image, Image2
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .functions import detect
from .functions import generate_images, generate_images_path, get_stored_dir, generate_jsonfile_path, generate_images_path_test, generate_jsonfile_path_test

import os, shutil

app_name = 'explorer'

# Create your views here.
def find_images(request):
    if request.method == 'POST':
        print('form post response received\n'*10) #test
        #fetch form response
        keywords = request.POST.get('keywords').replace(' ','_') #format

        assert keywords

        img_count = int(request.POST.get('count'))

        assert img_count

        dic=[keywords,img_count] #test

        stored_dir = get_stored_dir(keywords)
        generate_images(keywords,img_count,stored_dir, generate_images_path) #simple_images module
        path = generate_images_path
        #generate zip file
        shutil.make_archive(keywords, 'zip', path)
        #generate zip file path for client-side download
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



def remove_all_images(execution=True,path=None):
    if path == None: #default
        Image.objects.all().delete()
        parent_path = os.path.abspath('media') 
        images_path = os.path.join(parent_path,'images')  
    else: images_path = path #manual 

    all_images = os.listdir(images_path)

    for image in all_images:
        image_path = os.path.join(images_path,image)
        if execution: os.remove(image_path) #remove images
        else: pass #do nothing
    return all_images
    
def move_file(src,dest,cat='image'):
    allfiles = os.listdir(src)
    if cat=='image':
        for f in allfiles:
            src_path = os.path.join(src,f)
            dest_path = os.path.join(dest,f)
            os.replace(src_path, dest_path)
    elif cat=='file':
        src_path = os.path.join(src,allfiles[0])
        os.replace(src_path, dest)

from PIL import Image as im

def detection(request):
    django_img_path = None

    if request.method == 'POST':
        image = request.FILES['image']
        img_name = image.name

        #save received image
        image = im.open(image)
        parent_path = os.path.abspath('media') 
        images_path = os.path.join(parent_path,'images')
        if not os.path.exists(images_path): os.mkdir(images_path)
        img_path = os.path.join(images_path,img_name)
        image.save(img_path) 

        assert os.path.exists(img_path)

        #detect received image
        returned_image = detect(img_path) #ndarray
        returned_image = im.fromarray(returned_image) #convert to image
        
        #save detected image
        returned_image.save(img_path)
        django_img_path = f'/media/images/{img_name}'

    return render(request, "explorer/detection.html", {
        'img_path':django_img_path
    })

def train(request):
    all_images = [] #default empty
    store_dir = '' #defualt empty
    
    if request.method == "POST":
        print('form post image response received\n'*10) #test

        if request.FILES.getlist('images'): #image submitted

            #image handling
            images = request.FILES.getlist('images')
            for image in images:
                try: #prevent error
                    img_obj = Image.objects.create(title='none',image=image)
                    all_images.append(img_obj)
                except: pass

            images = request.FILES.getlist('images2')
            for image in images:
                try: #prevent error
                    img_obj = Image2.objects.create(title='none',image=image)
                    all_images.append(img_obj)
                except: pass

            #json file handling
            jsonfile = request.FILES['jsonfile']
            storage = FileSystemStorage()
            jsonfile_name = storage.save(jsonfile.name, jsonfile)
            store_dir = storage.url(jsonfile_name)

            jsonfile = request.FILES['jsonfile2']
            storage = FileSystemStorage()
            jsonfile_name = storage.save(jsonfile.name, jsonfile)
            store_dir = storage.url(jsonfile_name)
            
        else: #start training

            #change image file location 
            parent_path = os.path.abspath('media') 
            images_path = os.path.join(parent_path,'images')
            assert os.path.isdir(images_path)
            remove_all_images(execution=True,path=generate_images_path)
            move_file(images_path, generate_images_path)
            os.rmdir(images_path)

            parent_path = os.path.abspath('media') 
            images_path = os.path.join(parent_path,'images2')
            assert os.path.isdir(images_path)
            remove_all_images(execution=True,path=generate_images_path_test)
            move_file(images_path, generate_images_path_test)
            os.rmdir(images_path)

            # change json file location
            jsonfile_path = os.path.abspath('media')
            move_file(jsonfile_path, generate_jsonfile_path, 'file')

            jsonfile_path = os.path.abspath('media')
            move_file(jsonfile_path, generate_jsonfile_path_test, 'file')

            from .functions import main
            main()

    return render(request, 'explorer/train.html', {
        'images': all_images,
        'url': store_dir
    })

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
