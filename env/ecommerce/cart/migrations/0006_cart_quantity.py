# Generated by Django 5.0.3 on 2024-05-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0005_rename_quantity_cart_total"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="quantity",
            field=models.IntegerField(null=True),
        ),
    ]
