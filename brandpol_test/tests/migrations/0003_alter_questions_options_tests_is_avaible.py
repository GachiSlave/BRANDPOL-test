# Generated by Django 5.1 on 2024-08-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0002_questions"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="questions",
            options={"verbose_name": "Вопрос", "verbose_name_plural": "Вопросы"},
        ),
        migrations.AddField(
            model_name="tests",
            name="is_avaible",
            field=models.BooleanField(default=True),
        ),
    ]
