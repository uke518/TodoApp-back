# Generated by Django 4.1 on 2022-09-07 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todomodel',
            old_name='uuid',
            new_name='id',
        ),
    ]