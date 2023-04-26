# Generated by Django 4.1.6 on 2023-04-25 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
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
                ("title", models.CharField(max_length=50, verbose_name="タスク名")),
                ("detail", models.CharField(max_length=100, verbose_name="詳細")),
                ("registeDate", models.DateField(verbose_name="登録日")),
                ("priority", models.CharField(max_length=10, verbose_name="優先度")),
                ("validDate", models.DateField(verbose_name="有効期限")),
                ("complete", models.BooleanField(verbose_name="完了")),
            ],
        ),
    ]