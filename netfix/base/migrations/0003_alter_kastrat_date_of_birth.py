# Generated by Django 4.2 on 2023-05-01 08:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_kastrat_field_of_work_alter_kastrat_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kastrat',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2023, 5, 1)),
        ),
    ]