# Generated by Django 3.2.6 on 2022-09-06 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseReview', '0009_department_web'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='professor',
            field=models.ManyToManyField(blank=True, help_text='select a professor for the course', null=True, to='courseReview.professor'),
        ),
    ]