# Generated by Django 4.2.19 on 2025-03-01 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='desc',
        ),
    ]
