# Generated by Django 2.0 on 2019-04-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0009_auto_20190409_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_full', models.CharField(max_length=64)),
                ('state_short', models.CharField(max_length=2)),
            ],
        ),
    ]
