from django.contrib import admin
from django.urls import path

from . import views

app_name = 'recruiters'

urlpatterns = [
    path('', views.home, name='home'),
    path('new_job', views.new_job, name='new_job'), 
    
]
