# Generated by Django 3.2.6 on 2021-09-21 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210921_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='send_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 21, 5, 16, 24, 70382)),
        ),
    ]
