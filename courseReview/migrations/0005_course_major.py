# Generated by Django 3.2.6 on 2022-08-29 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseReview', '0004_auto_20220828_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='major',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courseReview.major'),
        ),
    ]
