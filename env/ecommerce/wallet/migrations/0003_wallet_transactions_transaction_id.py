# Generated by Django 5.0.3 on 2024-06-20 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wallet", "0002_wallet_transactions_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="wallet_transactions",
            name="transaction_id",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
