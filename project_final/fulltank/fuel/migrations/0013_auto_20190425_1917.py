# Generated by Django 2.0 on 2019-04-25 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0012_auto_20190425_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcshort',
            name='fuel',
            field=models.CharField(default=0, max_length=64),
        ),
        migrations.AlterField(
            model_name='fcshort',
            name='year',
            field=models.CharField(default=0, max_length=64),
        ),
        migrations.AlterField(
            model_name='fuelconsumption',
            name='fuel',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='states',
            name='state_short',
            field=models.CharField(max_length=64),
        ),
    ]
