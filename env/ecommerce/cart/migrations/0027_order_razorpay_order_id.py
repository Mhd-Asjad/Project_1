# Generated by Django 5.0.3 on 2024-06-07 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0026_payment"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="razorpay_order_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]