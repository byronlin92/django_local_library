# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 07:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20170831_0100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'permissions': (('can_edit_author', 'Edit author'),)},
        ),
    ]
