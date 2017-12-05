# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-30 15:41
from __future__ import unicode_literals

from django.db import migrations, models

from webodm import settings

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_public_task_uuids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='task',
            field=models.ForeignKey(null=False, on_delete=models.CASCADE, help_text="Task this image belongs to", to='app.Task')
        ),
    ]
