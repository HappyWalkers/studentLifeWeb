# Generated by Django 3.2.6 on 2022-09-06 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseReview', '0007_auto_20220831_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='web',
            field=models.URLField(blank=True, help_text='web used to verify the college', null=True, verbose_name='Official Website'),
        ),
    ]
