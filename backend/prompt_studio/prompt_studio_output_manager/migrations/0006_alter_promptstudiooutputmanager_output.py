# Generated by Django 4.2.1 on 2024-02-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "prompt_studio_output_manager",
            "0005_alter_promptstudiooutputmanager_profile_manager_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="promptstudiooutputmanager",
            name="output",
            field=models.CharField(
                blank=True, db_comment="Field to store output", null=True
            ),
        ),
    ]
