# Generated by Django 4.2.1 on 2024-02-13 11:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prompt_studio", "0003_remove_toolstudioprompt_updated_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="toolstudioprompt",
            name="prompt",
            field=models.TextField(
                blank=True, db_comment="Field to store the prompt"
            ),
        ),
    ]
