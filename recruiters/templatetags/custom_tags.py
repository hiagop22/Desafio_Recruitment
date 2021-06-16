from django import template
from ..models import Applicant

register = template.Library()

@register.simple_tag
def count_applicants(job_title):
    applicants_number = Applicant.objects.filter(job__title=job_title).count()
    return str(applicants_number)

@register.simple_tag
def insert_spaces_into_string(date):
    if 'semanas' in str(date):

        splited_time = str(date).split(',')
        if len(splited_time) == 2:
            num_in_date = [num for num in date if num.isdigit()]
            if num_in_date[0] == '1':
                week = 'semana'
            else:
                week = 'semanas'
            if num_in_date[1] == '1':
                day = 'dia'
            else:
                day = 'dias'
            date = f'{num_in_date[0]} {week}, {num_in_date[1]} {day} atrás'

    return date