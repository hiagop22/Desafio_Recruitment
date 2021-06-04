from django.core import paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from datetime import datetime

from .forms import JobForm
from .models import Job, Applicant

@login_required
def home(request):
    return render(request, 'recruiters/home.html')

@login_required()
def new_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user
            job.save()

            return redirect('/recruiters/list_jobs/')

    form = JobForm()
    return render(request, 'recruiters/new_job.html', {'form': form})

@login_required()
def list_jobs(request):
    job_list = Job.objects.filter(recruiter=request.user).order_by('-created_at')

    paginator = Paginator(job_list, 6)
    page_number = request.GET.get('page')
    jobs = paginator.get_page(page_number)
    print(type(jobs))
    return render(request, 'recruiters/list_jobs.html', {'jobs': jobs})

@login_required()
def view_job(request, id):
    job = get_object_or_404(Job, pk=id)
    return render(request, 'recruiters/view_job.html', {'job': job})

@login_required()
def update_job(request, id):
    job = get_object_or_404(Job, pk=id)
    form = JobForm(instance=job)

    if(request.method == 'POST'):
        job = JobForm(request.POST, instance=job)

        if(job.is_valid()):
            job.save()
            return redirect('/recruiters/list_jobs/')
        else:
            return render(request, 'recruiters/update_job.html', {'form': form})
    else:
        return render(request, 'recruiters/update_job.html', {'form': form})

@login_required()
def delete_job(request, id):
    job = get_object_or_404(Job, pk=id)

    job.delete()
    return redirect('/recruiters/list_jobs/')