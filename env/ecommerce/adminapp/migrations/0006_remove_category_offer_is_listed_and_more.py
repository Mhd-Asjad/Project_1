# Generated by Django 5.0.3 on 2024-06-10 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0005_category_offer_product_offer_delete_customer_coupon"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category_offer",
            name="is_listed",
        ),
        migrations.AlterField(
            model_name="category_offer",
            name="percentage",
            field=models.PositiveIntegerField(),
        ),
    ]