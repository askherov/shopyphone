# Generated by Django 5.0.1 on 2024-05-20 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_phone_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(upload_to='photos/phones/%Y/%m/%d/'),
        ),
    ]
