# Generated by Django 5.0.6 on 2024-06-25 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzez', '0005_remove_quiz_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
    ]
