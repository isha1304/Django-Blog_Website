# Generated by Django 4.2.4 on 2023-09-13 09:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Myapp", "0008_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Post",
            new_name="BlogPost",
        ),
    ]
