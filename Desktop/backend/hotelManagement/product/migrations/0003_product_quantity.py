# Generated by Django 4.1 on 2022-11-21 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_alter_cart_id_alter_category_id_alter_customer_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="quantity",
            field=models.IntegerField(default=None),
        ),
    ]
