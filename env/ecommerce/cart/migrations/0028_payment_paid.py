# Generated by Django 5.0.3 on 2024-06-08 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0027_order_razorpay_order_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="paid",
            field=models.BooleanField(default=False),
        ),
    ]
