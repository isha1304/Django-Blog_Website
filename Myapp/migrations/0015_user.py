# Generated by Django 4.2.4 on 2023-09-17 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Myapp", "0014_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("uid", models.CharField(max_length=20)),
                ("user_name", models.CharField(max_length=100)),
                ("uemail", models.EmailField(max_length=100)),
                ("ucontact", models.CharField(max_length=10)),
                ("upwd", models.CharField(max_length=8)),
            ],
            options={
                "db_table": "user",
            },
        ),
    ]
