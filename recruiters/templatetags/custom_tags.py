from django import template
from ..models import Applicant

register = template.Library()

@register.simple_tag
def count_applicants(job_title):
    applicants_number = Applicant.objects.filter(job__title=job_title).count()
    return str(applicants_number)