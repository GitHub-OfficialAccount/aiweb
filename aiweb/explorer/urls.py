from django.urls import path
from . import views

app_name = 'explorer'
urlpatterns = [
    path('', views.upload, name = 'upload'),
    path('show', views.show, name = 'show')
]