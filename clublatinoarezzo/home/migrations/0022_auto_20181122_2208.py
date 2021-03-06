# Generated by Django 2.1.2 on 2018-11-22 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20181122_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='testata',
            name='testata',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blog',
            name='nome',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='presentazione',
            name='label1',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='presentazione',
            name='label2',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='presentazione',
            name='label3',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='presentazione',
            name='label4',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='presentazionepunto',
            name='label1',
            field=models.TextField(blank=True, default='', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='servizi',
            name='label1',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='servizi',
            name='testo1',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='servizi',
            name='testo2',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='servizi',
            name='testo3',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='servizi',
            name='testo4',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='servizi',
            name='testo5',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='staff',
            name='nome',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
