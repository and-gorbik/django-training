# Generated by Django 2.1.5 on 2019-01-27 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190127_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='', max_length=100, unique=True, verbose_name='Title'),
        ),
    ]