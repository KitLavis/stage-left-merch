# Generated by Django 4.2.10 on 2024-03-08 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'get_latest_by': 'created_on'},
        ),
    ]