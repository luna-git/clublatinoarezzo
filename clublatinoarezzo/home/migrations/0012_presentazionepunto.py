# Generated by Django 2.1.2 on 2018-11-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_staff_staffdes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentazionepunto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label1', models.CharField(blank=True, default='', max_length=400, null=True)),
            ],
        ),
    ]