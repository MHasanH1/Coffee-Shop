# Generated by Django 4.2.5 on 2024-06-27 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_orderproduct_count_alter_product_coffee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='count',
        ),
    ]
