from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from .filehandler import handle_uploaded_file

app_name = 'explorer'

photos = []

# Create your views here.
def upload(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'explorer/upload.html', {
                'form': form, 
                'img_obj': img_obj
                })
    return render(request, 'explorer/upload.html', {
        'form': ImageForm()
        })

def show(request):
    return render(request,"explorer/show.html",{

    })