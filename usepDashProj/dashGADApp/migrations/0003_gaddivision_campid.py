# Generated by Django 5.0.6 on 2024-07-06 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashGADApp', '0002_alter_gadcampus_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='gaddivision',
            name='campId',
            field=models.CharField(default='', max_length=20),
        ),
    ]
