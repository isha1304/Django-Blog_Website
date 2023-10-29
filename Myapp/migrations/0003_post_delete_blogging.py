# Generated by Django 4.2.4 on 2023-09-13 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Myapp", "0002_alter_blogging_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("blog_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=1000)),
                ("content", models.TextField(blank=True, max_length=250, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("upload_to", models.DateTimeField(auto_now=True)),
                (
                    "date_posted",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Blogging",
        ),
    ]
