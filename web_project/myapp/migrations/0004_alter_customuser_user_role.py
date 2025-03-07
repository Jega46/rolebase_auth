# Generated by Django 5.1.1 on 2024-10-05 07:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_alter_paragraph_content_alter_paragraph_created_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_role",
            field=models.CharField(
                choices=[
                    ("admin", "Admin"),
                    ("viewer", "Viewer"),
                    ("editor", "editor"),
                ],
                max_length=10,
            ),
        ),
    ]
