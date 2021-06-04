import datetime
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from django.urls import reverse

from django.conf import settings

class Job(models.Model):
    FRESHMAN = 'FR'
    JUNIOR = 'JR'
    PLENO = 'PL'
    SENIOR = 'SR'

    SALARY_RANGE_CHOICES = [
        (FRESHMAN, 'Até 1.000'),
        (JUNIOR, 'De 1.000 a 2.000'),
        (PLENO, 'De 2.000 a 3.000'),
        (SENIOR, 'Acima de 3.000')
    ]

    ELEMENTARY = 'ELEMENTARY'
    HIGH = 'HIGH'
    TECHNOLOGIST = 'TECHNOLOGIST'
    COLLEGE = 'COLLEGE'
    MASTER = 'MASTER'
    DOCTORATE = 'DOCTORATE'

    COMPULSORY_SCHOOL_CHOICES = [
        (ELEMENTARY, 'Ensino fundamental'),
        (HIGH, 'Ensino médio'),
        (TECHNOLOGIST, 'Tecnólogo'),
        (COLLEGE, 'Ensino Superior'),
        (MASTER, 'Pós / MBA / Mestrado'),
        (DOCTORATE, 'Doutorado')
    ]

    recruiter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=255, verbose_name='Nome da Vaga', 
                    default='Título')
    salary_range = models.CharField(choices=SALARY_RANGE_CHOICES, max_length=2, 
                    verbose_name='Faixa Salarial')
    requirements = models.TextField(verbose_name='Requisitos')
    compulsory_school = models.CharField(choices=COMPULSORY_SCHOOL_CHOICES, max_length=255,
                    verbose_name='Escolaridade Mínima')

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    slug = AutoSlugField(unique=True, always_update=False, populate_from='title')

    @property
    def created_more_than_limit_days(self):
        limit_date = (timezone.now() - datetime.timedelta(days=30))

        if self.created_at < limit_date:
            return True
        return False
    
    # def get_absolute_url(self):
    #     return reverse()

    def __str__(self):
        return self.title

class Applicant(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    applicated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.applicant)