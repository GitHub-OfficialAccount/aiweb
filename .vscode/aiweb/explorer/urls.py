from django.urls import path
from . import views

app_name = 'explorer'
urlpatterns = [
    path('', views.Home, name = 'home'),
    path('upload', views.upload, name = 'upload'),
    path('show', views.show, name = 'show'),
    path('detection', views.detection, name = 'detection'),
    path('find_images', views.find_images, name = 'find_images'),
    path('train', views.train, name = 'train'),
    path('about', views.About, name = 'about'),
    path('what_is_AI', views.What_is_AI, name = 'what_is_AI'),
    path('steps', views.Steps, name = 'steps'),
    path('contact', views.Contact, name = 'contact')
]