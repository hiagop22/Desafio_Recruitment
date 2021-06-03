from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import JobForm
from .models import Job

# @login_required
def home(request):
    return render(request, 'recruiters/home.html')

# @login_required(login_url='')
def new_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)

        if form.is_valid():
            job = form.save()
            return redirect('new_job/')

    form = JobForm()
    return render(request, 'recruiters/new_job.html', {'form': form})

def list_jobs(request):
    jobs = Job.objects.filter(recruiter=request.user).order_by('-created_at')

    return render(request, 'recruiters/list_jobs.html', {'jobs': jobs})