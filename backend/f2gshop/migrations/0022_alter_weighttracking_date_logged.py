# Generated by Django 4.0.1 on 2023-02-21 16:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('f2gshop', '0021_alter_weighttracking_date_logged'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weighttracking',
            name='date_logged',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
