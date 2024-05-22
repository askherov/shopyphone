# Generated by Django 5.0.1 on 2024-05-13 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=64)),
                ('model_name', models.CharField(max_length=64)),
                ('battery', models.SmallIntegerField(default=0, help_text='mAh')),
                ('ram', models.CharField(choices=[('3', '3'), ('4', '4'), ('6', '6'), ('8', '8'), ('12', '12')], max_length=2)),
                ('memory', models.CharField(choices=[('32', '32'), ('64', '64'), ('128', '128'), ('264', '264'), ('512', '512'), ('1024', '1024')], help_text='GB', max_length=4)),
                ('is_new', models.BooleanField(default=False)),
                ('fingerprint', models.BooleanField(default=False)),
                ('fice_id', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='photos/cars/%Y/%m/%d/')),
                ('description', models.TextField(max_length=3000, null=True)),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='phones.color')),
            ],
        ),
    ]
