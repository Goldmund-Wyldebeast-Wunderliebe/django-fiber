# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import fiber.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fiber', '0002_auto_20150701_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentitem',
            name='content_html_en',
            field=fiber.utils.fields.FiberHTMLField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='contentitem',
            name='content_html_nl',
            field=fiber.utils.fields.FiberHTMLField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='contentitem',
            name='content_html_zh',
            field=fiber.utils.fields.FiberHTMLField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='contentitem',
            name='content_markup_en',
            field=fiber.utils.fields.FiberMarkupField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='contentitem',
            name='content_markup_nl',
            field=fiber.utils.fields.FiberMarkupField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='contentitem',
            name='content_markup_zh',
            field=fiber.utils.fields.FiberMarkupField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='contentitem',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='name', blank=True),
        ),
        migrations.AddField(
            model_name='contentitem',
            name='name_nl',
            field=models.CharField(max_length=255, null=True, verbose_name='name', blank=True),
        ),
        migrations.AddField(
            model_name='contentitem',
            name='name_zh',
            field=models.CharField(max_length=255, null=True, verbose_name='name', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description of the page', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='description_nl',
            field=models.TextField(null=True, verbose_name='description of the page', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='description_zh',
            field=models.TextField(null=True, verbose_name='description of the page', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='name', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='name_nl',
            field=models.CharField(max_length=255, null=True, verbose_name='name', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='name_zh',
            field=models.CharField(max_length=255, null=True, verbose_name='name', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='page',
            name='title_nl',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='page',
            name='title_zh',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='page',
            name='url_en',
            field=fiber.utils.fields.FiberURLField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='url_nl',
            field=fiber.utils.fields.FiberURLField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='url_zh',
            field=fiber.utils.fields.FiberURLField(max_length=255, null=True, blank=True),
        ),
    ]
