# Generated by Django 2.1.2 on 2018-11-18 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_titolo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentazione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/media/')),
                ('label1', models.CharField(max_length=200)),
                ('label2', models.CharField(max_length=200)),
                ('label3', models.CharField(max_length=200)),
                ('label4', models.CharField(max_length=200)),
                ('video', models.CharField(max_length=200)),
            ],
        ),
    ]