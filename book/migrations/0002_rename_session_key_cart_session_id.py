# Generated by Django 4.2.19 on 2025-03-08 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='session_key',
            new_name='session_id',
        ),
    ]
