# Generated by Django 4.1.3 on 2022-11-10 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='inventory_quality',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
