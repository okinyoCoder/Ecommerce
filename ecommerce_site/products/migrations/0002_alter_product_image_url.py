# Generated by Django 5.1.5 on 2025-04-04 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.ImageField(blank='True', upload_to='product_photos/'),
        ),
    ]
