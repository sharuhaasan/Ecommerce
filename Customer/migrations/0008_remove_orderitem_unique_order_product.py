# Generated by Django 4.2.7 on 2023-12-03 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0007_alter_orderitem_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='orderitem',
            name='unique_order_product',
        ),
    ]
