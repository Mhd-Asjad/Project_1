# Generated by Django 5.0.3 on 2024-05-18 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("useracc", "0003_register_age"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="register",
            name="age",
        ),
    ]
