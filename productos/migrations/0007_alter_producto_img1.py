# Generated by Django 5.1.4 on 2025-03-26 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_alter_producto_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]
