# Generated by Django 3.1.4 on 2020-12-12 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=''),
        ),
    ]