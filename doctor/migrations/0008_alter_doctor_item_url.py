# Generated by Django 4.0.5 on 2022-06-27 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0007_alter_doctor_item_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="item_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
