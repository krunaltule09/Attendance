# Generated by Django 2.1.2 on 2019-03-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='panel',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
