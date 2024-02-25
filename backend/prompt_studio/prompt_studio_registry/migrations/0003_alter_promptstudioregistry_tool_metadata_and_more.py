# Generated by Django 4.2.1 on 2024-02-01 11:58

import prompt_studio.prompt_studio_registry.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "prompt_studio_registry",
            "0002_remove_promptstudioregistry_updated_at_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="promptstudioregistry",
            name="tool_metadata",
            field=prompt_studio.prompt_studio_registry.fields.ToolMetadataJSONField(
                db_column="tool_metadata",
                db_comment="Metadata from Prompt Studio",
                default=dict,
            ),
        ),
        migrations.AlterField(
            model_name="promptstudioregistry",
            name="tool_property",
            field=prompt_studio.prompt_studio_registry.fields.ToolPropertyJSONField(
                db_column="tool_property",
                db_comment="PROPERTIES of the tool",
                default=dict,
            ),
        ),
        migrations.AlterField(
            model_name="promptstudioregistry",
            name="tool_spec",
            field=prompt_studio.prompt_studio_registry.fields.ToolSpecJSONField(
                db_column="tool_spec",
                db_comment="SPEC of the tool",
                default=dict,
            ),
        ),
    ]
