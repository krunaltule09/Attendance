# Generated by Django 2.1.2 on 2019-03-19 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_subjects'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subjects',
            new_name='Subject',
        ),
    ]
