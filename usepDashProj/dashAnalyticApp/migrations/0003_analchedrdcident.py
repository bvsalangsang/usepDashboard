# Generated by Django 5.0.6 on 2024-05-31 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashAnalyticApp', '0002_analboardpassers_analemployability'),
    ]

    operations = [
        migrations.CreateModel(
            name='analChedRdcIdent',
            fields=[
                ('ctrlNo', models.AutoField(primary_key=True, serialize=False)),
                ('analId', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('noOfUnderGrad', models.CharField(max_length=100)),
                ('noOfChedRdcIdent', models.CharField(max_length=100)),
                ('percentage', models.CharField(max_length=100)),
                ('isActive', models.CharField(default='Y', max_length=1)),
            ],
            options={
                'db_table': 'anal_ched_rdc',
            },
        ),
    ]
