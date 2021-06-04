from os import name
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'recruiters'

urlpatterns = [
    path('', views.home, name='home'),
    path('new_job/', views.new_job, name='new_job'), 
    path('list_jobs/', views.list_jobs, name='list_jobs'),
    path('view_job/<int:id>/', views.view_job, name='view_job'),
    path('update_job/<int:id>/', views.update_job, name='update_job'),
    path('delete_job/<int:id>/', views.delete_job, name='delete_job'),

]
