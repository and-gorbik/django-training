# Generated by Django 2.1.5 on 2019-01-24 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Title')),
                ('description', models.TextField(default='', verbose_name='Description')),
                ('added_at', models.DateField(auto_now_add=True, verbose_name='Added at')),
            ],
            options={
                'ordering': ['added_at'],
            },
        ),
    ]
