# Generated by Django 4.1 on 2022-11-21 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0005_rename_created_date_productorder_created_at_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ProductOrder",
        ),
    ]
