# Generated by Django 5.0.6 on 2024-10-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="news_details",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("news_category", models.CharField(default="dummy", max_length=255)),
                ("news_topic", models.CharField(default="dummy", max_length=255)),
                ("search_input_term", models.TextField()),
                ("last_updated", models.DateTimeField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="sentiment_results",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("news_category", models.CharField(default="dummy", max_length=255)),
                ("news_topic", models.CharField(default="dummy", max_length=255)),
                ("news_text", models.CharField(default="dummy", max_length=255)),
                ("news_published_at", models.DateTimeField(default=None, null=True)),
                ("news_saved_at", models.DateTimeField(default=None, null=True)),
                ("news_link", models.CharField(default="dummy", max_length=255)),
                ("sentiment_score", models.FloatField(default=-999)),
                ("sentiment_value", models.CharField(default="none", max_length=255)),
            ],
        ),
    ]
