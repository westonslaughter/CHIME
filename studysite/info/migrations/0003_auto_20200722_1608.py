# Generated by Django 3.0.3 on 2020-07-22 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20200722_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='org',
            name='url',
            field=models.URLField(default='www.google.com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='title',
            field=models.CharField(default='Researcher', max_length=256),
            preserve_default=False,
        ),
    ]
