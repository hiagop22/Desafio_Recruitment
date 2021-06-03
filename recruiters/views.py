from django.shortcuts import redirect, render, get_object_or_404
from .forms import NewJob

def home(request):
    return render(request, 'recruiters/home.html')

def new_job(request):
    if request.method == 'POST':
        form = NewJob(request.POST)

        if form.is_valid():
            job = form.save()
            return redirect('new_job/')

    form = NewJob()
    return render(request, 'recruiters/new_job.html', {'form': form})