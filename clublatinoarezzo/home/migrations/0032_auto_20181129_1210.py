# Generated by Django 2.1.2 on 2018-11-29 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_auto_20181127_1436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogdes',
            options={'verbose_name_plural': 'Blog-descrizione'},
        ),
        migrations.AlterModelOptions(
            name='footeradv',
            options={'verbose_name_plural': 'Footer-adv'},
        ),
        migrations.AlterModelOptions(
            name='presentazione',
            options={'verbose_name': 'Presentazione', 'verbose_name_plural': 'Presentazione'},
        ),
        migrations.AlterModelOptions(
            name='presentazionepunto',
            options={'verbose_name': 'Presentazione-punto', 'verbose_name_plural': 'Presentazione-punti'},
        ),
        migrations.AlterModelOptions(
            name='testata',
            options={'verbose_name': 'Testata', 'verbose_name_plural': 'Testata'},
        ),
        migrations.AlterModelOptions(
            name='titolo',
            options={'verbose_name': 'Titolo', 'verbose_name_plural': 'Titoli'},
        ),
    ]