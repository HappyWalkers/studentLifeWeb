# Generated by Django 3.2.6 on 2022-08-28 14:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_profile_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='college',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='enter the name of the college', max_length=20)),
                ('introduction', models.TextField(help_text='enter a brief introduction of the college', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='enter the name of the course', max_length=200)),
                ('introduction', models.TextField(help_text='enter a brief introduction of the course', max_length=1000)),
                ('rating', models.IntegerField(blank=True, help_text='average score of the course rating', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseReview.college')),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='enter the name of the department', max_length=200)),
                ('introduction', models.TextField(help_text='enter a brief introduction of the department', max_length=1000)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseReview.college')),
            ],
        ),
        migrations.CreateModel(
            name='extendUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basicUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('college', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courseReview.college')),
                ('courses', models.ManyToManyField(blank=True, help_text='courses taken by the user', to='courseReview.course')),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True, help_text='enter a review for the course', max_length=1000)),
                ('time', models.TimeField(auto_now_add=True)),
                ('rating', models.IntegerField(help_text='rate this course', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('score', models.IntegerField(blank=True, help_text='enter your score of the course', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('qualityRating', models.IntegerField(help_text='rate the qulaity of the course', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseReview.course')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courseReview.extenduser')),
            ],
        ),
        migrations.CreateModel(
            name='professor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='enter the name of the professor', max_length=200)),
                ('introduction', models.TextField(help_text='enter a brief introduction of the professor', max_length=1000)),
                ('rating', models.IntegerField(blank=True, help_text='average score of the courses ratings which taught by the professor', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseReview.college')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseReview.department')),
            ],
        ),
        migrations.CreateModel(
            name='major',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='enter the name of the major', max_length=200)),
                ('introduction', models.TextField(help_text='enter a brief introduction of the major', max_length=1000)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseReview.college')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseReview.department')),
            ],
        ),
        migrations.AddField(
            model_name='extenduser',
            name='major',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courseReview.major'),
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseReview.department'),
        ),
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.ManyToManyField(help_text='select a professor for the course', to='courseReview.professor'),
        ),
    ]
