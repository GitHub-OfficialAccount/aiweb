from django.urls import path
from . import views

app_name = 'explorer'
urlpatterns = [
    path('upload', views.upload, name = 'upload'),
    path('show', views.show, name = 'show'),
    path('detection', views.detection, name='detection'),
    path('find_images', views.find_images, name='find_images')
]