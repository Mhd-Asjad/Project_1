# Generated by Django 5.0.3 on 2024-06-03 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0022_alter_order_items_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="order_items",
            name="request_return",
            field=models.BooleanField(default=False),
        ),
    ]
