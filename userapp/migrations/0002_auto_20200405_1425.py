# Generated by Django 3.0.4 on 2020-04-05 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='tz',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
