# Generated by Django 4.0.1 on 2022-01-31 15:28

import django.contrib.postgres.fields
from django.db import migrations, models
import puzzles.models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0004_alter_puzzle_solution'),
    ]

    operations = [
        migrations.RenameField(
            model_name='puzzle',
            old_name='question',
            new_name='ques',
        ),
        migrations.RemoveField(
            model_name='puzzle',
            name='solution',
        ),
        migrations.AddField(
            model_name='puzzle',
            name='sol',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=puzzles.models.get_default), size=9), default=puzzles.models.get_default, size=9),
        ),
    ]
