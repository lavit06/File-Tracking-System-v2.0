# Generated by Django 4.2.11 on 2024-05-22 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fts_app", "0006_userdetail_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdetail",
            name="full_name",
            field=models.CharField(max_length=255, null=True),
        ),
    ]