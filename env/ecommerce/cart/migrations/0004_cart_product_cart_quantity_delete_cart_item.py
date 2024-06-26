# Generated by Django 5.0.3 on 2024-05-05 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0003_remove_cart_cart_id_alter_cart_item_cart"),
        ("products", "0007_alter_addimages_image1_alter_addimages_image2_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="products.product",
            ),
        ),
        migrations.AddField(
            model_name="cart",
            name="quantity",
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name="Cart_item",
        ),
    ]
