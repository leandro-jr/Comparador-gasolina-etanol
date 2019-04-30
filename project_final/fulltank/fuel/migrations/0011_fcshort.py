# Generated by Django 2.0 on 2019-04-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0010_states'),
    ]

    operations = [
        migrations.CreateModel(
            name='FCShort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(default=0, max_length=4)),
                ('brand', models.CharField(default=0, max_length=64)),
                ('model', models.CharField(default=0, max_length=64)),
                ('engine', models.CharField(default=0, max_length=64)),
                ('version', models.CharField(default=0, max_length=64)),
                ('fuel', models.CharField(default=0, max_length=1)),
                ('km_per_liter_ethanol_city', models.FloatField(default=0)),
                ('km_per_liter_ethanol_road', models.FloatField(default=0)),
                ('km_per_liter_gas_city', models.FloatField(default=0)),
                ('km_per_liter_gas_road', models.FloatField(default=0)),
            ],
        ),
    ]
