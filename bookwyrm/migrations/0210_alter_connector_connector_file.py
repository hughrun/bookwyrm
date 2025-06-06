# Generated by Django 4.2.17 on 2025-02-02 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0209_user_show_ratings"),
    ]

    operations = [
        migrations.AlterField(
            model_name="connector",
            name="connector_file",
            field=models.CharField(
                choices=[
                    ("openlibrary", "Openlibrary"),
                    ("inventaire", "Inventaire"),
                    ("bookwyrm_connector", "Bookwyrm Connector"),
                    ("finna", "Finna"),
                ],
                max_length=255,
            ),
        ),
    ]
