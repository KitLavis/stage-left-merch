# Generated by Django 4.2.10 on 2024-02-25 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_full_name_order_original_basket_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='full_name',
        ),
    ]
