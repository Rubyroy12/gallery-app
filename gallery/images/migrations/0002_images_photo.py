# Generated by Django 3.2.4 on 2021-07-01 19:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/'),
            preserve_default=False,
        ),
    ]
