# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import fiber.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fiber', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='description',
            field=models.TextField(null=True, verbose_name='description of the page', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name', blank=True),
        ),
    ]
