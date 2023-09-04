# Generated by Django 4.2 on 2023-06-09 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Adminapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Userinfo",
            fields=[
                (
                    "username",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("email", models.EmailField(max_length=50)),
                ("password", models.CharField(max_length=20)),
            ],
        ),
    ]
