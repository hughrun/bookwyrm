# Generated by Django 4.2.15 on 2024-08-24 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0208_merge_0207_merge_20240629_0626_0207_sqlparse_update"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="show_ratings",
            field=models.BooleanField(default=True),
        ),
    ]
