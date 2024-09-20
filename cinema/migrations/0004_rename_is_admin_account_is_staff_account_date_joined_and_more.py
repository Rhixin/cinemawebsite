# Generated by Django 5.1.1 on 2024-09-20 04:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cinema", "0003_rename_user_profile_account"),
    ]

    operations = [
        migrations.RenameField(
            model_name="account",
            old_name="is_admin",
            new_name="is_staff",
        ),
        migrations.AddField(
            model_name="account",
            name="date_joined",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="account",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
