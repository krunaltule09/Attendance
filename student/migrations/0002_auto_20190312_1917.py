# Generated by Django 2.1.2 on 2019-03-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='att_ds2',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='att_ic',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='att_mmc',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='att_os',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='att_sepm',
            field=models.IntegerField(blank=True),
        ),
    ]
