# Generated by Django 4.0.5 on 2022-06-27 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0006_alter_doctor_item_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="item_url",
            field=models.URLField(null=True),
        ),
    ]