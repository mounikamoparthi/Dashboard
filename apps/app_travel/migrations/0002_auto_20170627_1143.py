# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0001_initial'),
        ('app_travel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.RemoveField(
            model_name='trip',
            name='travellers',
        ),
        migrations.AddField(
            model_name='trip',
            name='travellers',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='travellers', to='app_login.User'),
            preserve_default=False,
        ),
    ]
