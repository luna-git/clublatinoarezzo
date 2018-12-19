# Generated by Django 2.1.2 on 2018-11-28 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181128_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articoloblog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(blank=True, default='', max_length=300)),
                ('testo', models.TextField(blank=True, default='', null=True)),
                ('immagine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Fotoblog', to='blog.Image')),
            ],
        ),
        migrations.RenameModel(
            old_name='Blog',
            new_name='Testatablog',
        ),
    ]
