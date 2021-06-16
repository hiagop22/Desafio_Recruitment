from django.core import paginator
from django.shortcuts import render
from recruiters.models import Job
from django.core.paginator import Paginator

def list_jobs(request):
    job_list = Job.objects.filter().order_by('created_at')

    paginator = Paginator(job_list, 6)
    page_number = request.GET.get('page')
    jobs = paginator.get_page(page_number)

    return render(request, 'candidates/list_jobs.html', {'jobs': jobs})
