# Generated by Django 5.0.3 on 2024-06-10 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0010_alter_productsize_size"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="offer_price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
