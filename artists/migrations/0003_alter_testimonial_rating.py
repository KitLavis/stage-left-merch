# Generated by Django 4.2.10 on 2024-03-01 09:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_alter_testimonial_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='rating',
            field=models.PositiveIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
