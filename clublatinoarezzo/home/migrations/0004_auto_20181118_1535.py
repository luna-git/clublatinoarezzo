# Generated by Django 2.1.2 on 2018-11-18 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20181118_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testata',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/'),
        ),
    ]
