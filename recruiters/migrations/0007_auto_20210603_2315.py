# Generated by Django 3.2.3 on 2021-06-03 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiters', '0006_applicant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='update_at',
            field=models.DateField(auto_now=True),
        ),
    ]