# Generated by Django 2.0 on 2019-03-21 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FuelConsumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=64)),
                ('model', models.CharField(max_length=64)),
                ('version', models.CharField(max_length=255)),
                ('fuel', models.CharField(max_length=1)),
                ('km_per_liter_ethanol_city', models.FloatField()),
                ('km_per_liter_ethanol_road', models.FloatField()),
                ('km_per_liter_gas_city', models.FloatField()),
                ('km_per_liter_gas_road', models.FloatField()),
            ],
        ),
    ]
