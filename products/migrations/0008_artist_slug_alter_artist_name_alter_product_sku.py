# Generated by Django 4.2.10 on 2024-02-15 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_artist_product_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.SlugField(default='na', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]
