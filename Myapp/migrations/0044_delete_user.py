# Generated by Django 4.2.4 on 2023-10-29 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Myapp", "0043_alter_post_snippet_delete_comment"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]
