from django import template
from ..models import Applicant

register = template.Library()

@register.simple_tag
def count_applicants(job_title):
    applicants_number = Applicant.objects.filter(job__title=job_title).count()
    return str(applicants_number)

@register.simple_tag
def remove_hour_if_there_is_day(date):
    splited_time = str(date).split(',')
    if len(splited_time) == 2:
        return f'{splited_time[0]} atrás'
    return splited_time[0]