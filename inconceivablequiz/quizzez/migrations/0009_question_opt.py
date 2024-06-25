# Generated by Django 5.0.6 on 2024-06-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzez', '0008_remove_quiz_questions_question_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='opt',
            field=models.CharField(choices=[('1', 'A'), ('2', 'B'), ('3', 'C'), ('4', 'D')], default='1', max_length=50),
        ),
    ]
