# Generated by Django 4.2 on 2023-08-13 09:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("news", "0002_alter_comments_options_alter_news_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="likes",
            field=models.ManyToManyField(
                blank=True,
                related_name="likes",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Лайки",
            ),
        ),
    ]
