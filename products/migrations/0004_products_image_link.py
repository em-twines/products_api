# Generated by Django 4.1.3 on 2022-11-10 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_products_inventory_quality_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image_link',
            field=models.CharField(default='https://assets-eu-01.kc-usercontent.com/559bb7d3-88a4-01c1-79a3-dd4d5b2d2bb0/b952b71e-20ff-4434-9486-5aa0b4378145/1-French-Baguettes.jpg?w=1920&q=85&auto=format&lossless=1', max_length=255),
        ),
    ]