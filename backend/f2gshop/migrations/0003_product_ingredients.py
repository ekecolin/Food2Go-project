# Generated by Django 4.0.1 on 2022-11-19 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f2gshop', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.TextField(null=True),
        ),
    ]