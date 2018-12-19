# Generated by Django 2.1.2 on 2018-11-22 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20181121_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servizi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/media/')),
                ('label1', models.CharField(blank=True, default='', max_length=100)),
                ('testo1', models.CharField(blank=True, default='', max_length=100)),
                ('label2', models.CharField(blank=True, default='', max_length=100)),
                ('testo2', models.CharField(blank=True, default='', max_length=100)),
                ('label3', models.CharField(blank=True, default='', max_length=100)),
                ('testo3', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='blogdes',
            name='label1',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blogdes',
            name='label2',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='footeradv',
            name='label1',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='footeradv',
            name='label2',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='staffdes',
            name='label1',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='staffdes',
            name='label2',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='testata',
            name='label1',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='testata',
            name='label2',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='testata',
            name='label3',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='testata',
            name='label4',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='titolo',
            name='email',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='titolo',
            name='indirizzo',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='titolo',
            name='label1',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='titolo',
            name='label2',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='titolo',
            name='linkfacebook',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='titolo',
            name='linkinstagram',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='titolo',
            name='linktwitter',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='titolo',
            name='telefono',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
