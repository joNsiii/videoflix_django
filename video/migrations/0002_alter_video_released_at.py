# Generated by Django 5.1 on 2024-08-09 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='released_at',
            field=models.DateTimeField(verbose_name=datetime.date(2024, 8, 9)),
        ),
    ]
