# Generated by Django 4.2.5 on 2024-06-27 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_order_purchase_amount_alter_order_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='purchase_amount',
        ),
    ]