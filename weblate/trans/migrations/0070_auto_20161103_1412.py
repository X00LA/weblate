# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-03 13:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0069_source_screenshot'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='source',
            options={'permissions': (('edit_priority', 'Can edit priority'), ('edit_flags', 'Can edit check flags'), ('upload_screenshot', 'Can upload screenshot'))},
        ),
    ]
