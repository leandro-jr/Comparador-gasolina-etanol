# Generated by Django 2.0 on 2019-04-05 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0003_cities'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuelconsumption',
            name='year',
            field=models.PositiveSmallIntegerField(default=2019),
            preserve_default=False,
        ),
    ]
