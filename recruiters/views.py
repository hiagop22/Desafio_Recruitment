from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, 'recruiters/home.html')

def new_job(request):

    return render(request, 'recruiters/new_job.html')