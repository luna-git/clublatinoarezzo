# Generated by Django 2.1.2 on 2018-11-28 15:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_articoloblog_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoriablog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categorie',
            },
        ),
        migrations.AlterModelOptions(
            name='articoloblog',
            options={'verbose_name': 'Articolo', 'verbose_name_plural': 'Articoli'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Immagine', 'verbose_name_plural': 'Immagini'},
        ),
        migrations.AlterModelOptions(
            name='testatablog',
            options={'verbose_name': 'Testata', 'verbose_name_plural': 'Testata'},
        ),
        migrations.AddField(
            model_name='articoloblog',
            name='categoria',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='Typeart', to='blog.Image'),
            preserve_default=False,
        ),
    ]