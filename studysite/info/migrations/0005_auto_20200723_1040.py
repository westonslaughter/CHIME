# Generated by Django 3.0.3 on 2020-07-23 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_staff_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(default='NoPho.jpg', upload_to=None),
        ),
    ]
