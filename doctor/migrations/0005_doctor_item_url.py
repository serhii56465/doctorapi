# Generated by Django 4.0.5 on 2022-06-27 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0004_remove_doctor_item_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="item_url",
            field=models.URLField(default="def", unique=True),
        ),
    ]
