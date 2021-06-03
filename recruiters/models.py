from django.db import models

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

    recruiter = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Nome da Vaga')
    salary_range = models.CharField(choices=SALARY_RANGE_CHOICES, max_length=2, 
                    verbose_name='Faixa Salarial')
    requirements = models.TextField(verbose_name='Requisitos')
    compulsory_school = models.CharField(choices=COMPULSORY_SCHOOL_CHOICES, max_length=255,
                    verbose_name='Escolaridade Mínima')


