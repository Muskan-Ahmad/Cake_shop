# Generated by Django 4.2 on 2023-08-29 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Userapp", "0006_alter_ordermaster_dateoforder"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ordermaster",
            name="dateoforder",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 30, 0, 49, 11, 126920)
            ),
        ),
    ]
