# Generated by Django 4.0.1 on 2023-01-22 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f2gshop', '0013_alter_basket_id_alter_basketitem_id_alter_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='postcode',
            field=models.TextField(default=''),
        ),
    ]
