# Generated by Django 4.2 on 2023-08-12 16:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comments",
            options={
                "ordering": ("id",),
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
            },
        ),
        migrations.AlterModelOptions(
            name="news",
            options={
                "ordering": ("id",),
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
            },
        ),
    ]
