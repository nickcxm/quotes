# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-03 04:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='Tags',
            new_name='tags',
        ),
    ]
