# Generated by Django 3.1.4 on 2020-12-14 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_contact_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='number',
            field=models.CharField(default='', max_length=15),
        ),
    ]
