# Generated by Django 4.0.1 on 2022-02-20 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0011_puzzle_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='bestTime_minutes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='bestTime_seconds',
            field=models.IntegerField(default=0),
        ),
    ]
