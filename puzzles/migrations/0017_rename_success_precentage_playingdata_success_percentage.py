# Generated by Django 4.0.1 on 2022-03-11 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0016_rename_win_precentage_playingdata_success_precentage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playingdata',
            old_name='success_precentage',
            new_name='success_percentage',
        ),
    ]