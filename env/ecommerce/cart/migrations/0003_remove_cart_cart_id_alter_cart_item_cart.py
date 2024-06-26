# Generated by Django 5.0.3 on 2024-05-05 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0002_cart_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="cart_id",
        ),
        migrations.AlterField(
            model_name="cart_item",
            name="cart",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="cart.cart",
            ),
        ),
    ]
