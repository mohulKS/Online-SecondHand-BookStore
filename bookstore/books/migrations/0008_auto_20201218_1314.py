# Generated by Django 3.1.4 on 2020-12-18 07:44

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20201218_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default=True, max_length=255, verbose_name='image'),
        ),
    ]
