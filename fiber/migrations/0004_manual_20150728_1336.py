# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import fiber.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fiber', '0003_auto_20150728_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='meta_keywords',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='doc_title',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
