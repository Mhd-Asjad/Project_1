# Generated by Django 5.0.3 on 2024-05-25 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0009_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="tracking_id",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
