# Generated by Django 5.0.6 on 2024-08-07 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashStrategicApp', '0003_stratyearlyscorecard'),
    ]

    operations = [
        migrations.CreateModel(
            name='stratTemplate',
            fields=[
                ('tempId', models.AutoField(primary_key=True, serialize=False)),
                ('tempName', models.CharField(max_length=50)),
                ('createdBy', models.CharField(max_length=20)),
                ('createdDate', models.DateField()),
                ('isActive', models.CharField(default='Y', max_length=1)),
            ],
            options={
                'db_table': 'strat_template',
            },
        ),
        migrations.CreateModel(
            name='stratTemplateDet',
            fields=[
                ('ctrlNo', models.AutoField(primary_key=True, serialize=False)),
                ('tempId', models.CharField(max_length=20)),
                ('indId', models.CharField(max_length=20)),
                ('reference', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=30)),
                ('target', models.CharField(max_length=20)),
                ('isActive', models.CharField(default='Y', max_length=1)),
            ],
            options={
                'db_table': 'strat_template_det',
            },
        ),
        migrations.RenameField(
            model_name='stratyearlyscorecard',
            old_name='year',
            new_name='targetyear',
        ),
        migrations.AddField(
            model_name='stratyearlyscorecard',
            name='reference',
            field=models.CharField(default='', max_length=30),
        ),
    ]
