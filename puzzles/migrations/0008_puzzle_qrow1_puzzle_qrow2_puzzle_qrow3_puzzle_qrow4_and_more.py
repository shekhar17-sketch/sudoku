# Generated by Django 4.0.1 on 2022-02-01 11:03

import django.contrib.postgres.fields
from django.db import migrations, models
import puzzles.models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0007_remove_puzzle_question_remove_puzzle_sol'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='qrow1',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=puzzles.models.get_default, size=9),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='qrow2',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=puzzles.models.get_default, size=9),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='qrow3',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=puzzles.models.get_default, size=9),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='qrow4',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=puzzles.models.get_default, size=9),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='qrow5',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=puzzles.models.get_default, size=9),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='qrow6',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=puzzles.models.get_default, size=9),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='qrow7',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=puzzles.models.get_default, size=9),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='qrow8',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=puzzles.models.get_default, size=9),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='qrow9',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=puzzles.models.get_default, size=9),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='srow1',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=puzzles.models.get_default, size=9),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='srow2',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=puzzles.models.get_default, size=9),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='srow3',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=puzzles.models.get_default, size=9),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='srow4',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=puzzles.models.get_default, size=9),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='srow5',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=puzzles.models.get_default, size=9),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='srow6',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=puzzles.models.get_default, size=9),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='srow7',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=puzzles.models.get_default, size=9),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='srow8',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=puzzles.models.get_default, size=9),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='srow9',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=puzzles.models.get_default, size=9),
        ),
    ]