# Generated by Django 2.1.2 on 2018-11-18 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_testata_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testata',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='home/static/home/media/'),
        ),
    ]
