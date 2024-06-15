# Generated by Django 5.0.3 on 2024-06-02 07:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0002_category_is_deleted_category_is_listed"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Coupon",
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
                ("coupon_code", models.CharField(max_length=100, unique=True)),
                ("coupon_name", models.CharField(max_length=50)),
                ("discount_percentage", models.IntegerField(default=0)),
                ("minimum_amnt", models.PositiveBigIntegerField(blank=True, default=0)),
                ("max_amount", models.PositiveBigIntegerField(blank=True, default=0)),
                ("is_active", models.BooleanField(default=True)),
                ("added_date", models.DateTimeField(auto_now_add=True)),
                ("starting_date", models.DateTimeField(blank=True, null=True)),
                ("expiry_date", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Customer_coupon",
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
                ("added_date", models.DateTimeField(auto_now_add=True)),
                (
                    "coupon",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="adminapp.coupon",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]