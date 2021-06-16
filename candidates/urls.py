from django.urls import path

from . import views

app_name = 'candidates'

urlpatterns = [
    # path('', views.home, name='home'),
    path('list_jobs/', views.list_jobs, name='list_jobs'),
    # path('<slug:slug>/', views.view_job, name='detail_job'),
    # path('<slug:slug>/update_job/', views.update_job, name='update_job'),
    # path('<slug:slug>/delete_job/', views.delete_job, name='delete_job'),

]
