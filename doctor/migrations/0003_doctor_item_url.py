# Generated by Django 4.0.5 on 2022-06-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0002_alter_doctor_birthday"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="item_url",
            field=models.URLField(default="name"),
        ),
    ]
