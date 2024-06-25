# Generated by Django 5.0.6 on 2024-06-25 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzez', '0007_quiz_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='questions',
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='quizzez.quiz'),
            preserve_default=False,
        ),
    ]
