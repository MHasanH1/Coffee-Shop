# Generated by Django 4.2.5 on 2024-06-24 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='vertical',
            field=models.CharField(choices=[('hot drink', 'Hot Drink'), ('cold drink', 'Cold Drink'), ('cake', 'Cake')], max_length=100),
        ),
    ]
