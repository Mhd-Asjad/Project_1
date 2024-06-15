# Generated by Django 5.0.3 on 2024-06-10 10:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0004_remove_coupon_starting_date"),
        ("products", "0010_alter_productsize_size"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category_offer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("percentage", models.IntegerField()),
                ("is_listed", models.BooleanField(default=True)),
                (
                    "cat_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="adminapp.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product_offer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("percentage", models.IntegerField()),
                ("is_listed", models.BooleanField(default=True)),
                (
                    "prod_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Customer_coupon",
        ),
    ]