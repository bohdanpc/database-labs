# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-25 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoolApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SurveyResults',
            new_name='SurveyResult',
        ),
    ]
