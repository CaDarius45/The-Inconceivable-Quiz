# Generated by Django 5.0.6 on 2024-06-26 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('quizzez', '0012_rename_customuser_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CustomUser',
        ),
    ]
