# Generated by Django 4.2.4 on 2023-10-29 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Myapp", "0044_delete_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="snippet",
            field=models.CharField(
                default="Write a snippet for your post here!!", max_length=800
            ),
        ),
    ]
