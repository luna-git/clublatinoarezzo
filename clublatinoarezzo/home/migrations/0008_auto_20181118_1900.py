# Generated by Django 2.1.2 on 2018-11-18 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20181118_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentazione',
            name='label1',
            field=models.CharField(default='', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='presentazione',
            name='label2',
            field=models.CharField(default='', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='presentazione',
            name='label3',
            field=models.CharField(default='', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='presentazione',
            name='label4',
            field=models.CharField(default='', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='presentazione',
            name='video',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
