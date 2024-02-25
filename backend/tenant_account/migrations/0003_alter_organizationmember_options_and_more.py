# Generated by Django 4.2.1 on 2023-09-15 12:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tenant_account", "0002_organizationmember_delete_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="organizationmember",
            options={},
        ),
        migrations.AlterModelManagers(
            name="organizationmember",
            managers=[],
        ),
        migrations.RenameField(
            model_name="organizationmember",
            old_name="user_ptr",
            new_name="user",
        ),
        migrations.AlterField(
            model_name="organizationmember",
            name="user",
            field=models.OneToOneField(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="organization_member",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="organizationmember",
            name="member_id",
            field=models.BigAutoField(
                auto_created=True,
                default=None,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="organizationmember",
            name="role",
            field=models.CharField(),
        ),
    ]
