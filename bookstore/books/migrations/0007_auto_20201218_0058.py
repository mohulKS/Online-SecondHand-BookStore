# Generated by Django 3.1.4 on 2020-12-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
