# Generated by Django 2.1.2 on 2018-12-07 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181129_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articoloblog',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Typeart', to='blog.Categoriablog'),
        ),
    ]
