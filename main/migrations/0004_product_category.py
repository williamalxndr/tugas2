# Generated by Django 5.1.1 on 2024-10-01 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('elektronik', 'Elektronik'), ('fashion', 'Fashion & Style'), ('makanan', 'Makanan & Minuman'), ('furniture', 'Furniture'), ('otomotif', 'Otomotif'), ('alattulis', 'Alat Tulis'), ('others', 'Others')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
