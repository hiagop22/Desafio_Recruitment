from django.core import paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

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
    job_list = Job.objects.filter(recruiter=request.user).order_by('-created_at')

    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page')
    jobs = paginator.get_page(page_number)
    print(type(jobs))
    return render(request, 'recruiters/list_jobs.html', {'jobs': jobs})