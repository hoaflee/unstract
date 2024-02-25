# Generated by Django 4.2.1 on 2024-01-23 11:18

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("connector", "0001_initial"),
        ("workflow", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ToolInstance",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "tool_id",
                    models.CharField(
                        db_comment="Function name of the tool being used",
                        max_length=64,
                    ),
                ),
                (
                    "input",
                    models.JSONField(
                        db_comment="Provisional WF input to a tool", null=True
                    ),
                ),
                (
                    "output",
                    models.JSONField(
                        db_comment="Provisional WF output to a tool", null=True
                    ),
                ),
                ("version", models.CharField(max_length=16)),
                (
                    "metadata",
                    models.JSONField(db_comment="Stores config for a tool"),
                ),
                ("step", models.IntegerField()),
                (
                    "status",
                    models.CharField(default="Ready to start", max_length=32),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="created_tools",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "input_db_connector",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="input_db_connector",
                        to="connector.connectorinstance",
                    ),
                ),
                (
                    "input_file_connector",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="input_file_connector",
                        to="connector.connectorinstance",
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="modified_tools",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "output_db_connector",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="output_db_connector",
                        to="connector.connectorinstance",
                    ),
                ),
                (
                    "output_file_connector",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="output_file_connector",
                        to="connector.connectorinstance",
                    ),
                ),
                (
                    "workflow",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="workflow_tool",
                        to="workflow.workflow",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
