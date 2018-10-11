# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 07:36
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=image_cropping.fields.ImageCropField(blank=True, upload_to='uploaded_images'),
        ),
    ]
