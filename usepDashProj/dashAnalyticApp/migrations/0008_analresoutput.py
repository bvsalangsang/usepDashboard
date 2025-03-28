# Generated by Django 5.0.6 on 2024-06-03 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashAnalyticApp', '0007_analaccgradprog'),
    ]

    operations = [
        migrations.CreateModel(
            name='analResOutput',
            fields=[
                ('ctrlNo', models.AutoField(primary_key=True, serialize=False)),
                ('analId', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('noOfResOutput', models.CharField(max_length=100)),
                ('isActive', models.CharField(default='Y', max_length=1)),
            ],
            options={
                'db_table': 'anal_res_output',
            },
        ),
    ]
