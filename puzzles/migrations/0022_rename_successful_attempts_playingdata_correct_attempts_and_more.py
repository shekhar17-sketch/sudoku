# Generated by Django 4.0.1 on 2022-03-13 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0021_dificultylevel_number_of_empty_cells'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playingdata',
            old_name='successful_attempts',
            new_name='correct_attempts',
        ),
        migrations.RenameField(
            model_name='playingdata',
            old_name='unsuccessful_attempts',
            new_name='incorrect_attempts',
        ),
        migrations.RenameField(
            model_name='playingdata',
            old_name='success_percentage',
            new_name='successrate',
        ),
    ]
