# Generated by Django 4.2 on 2023-07-03 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Userapp", "0003_ordermaster_details_alter_ordermaster_dateoforder"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ordermaster",
            name="dateoforder",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 3, 18, 45, 39, 753620)
            ),
        ),
    ]
