# Generated by Django 5.1.4 on 2025-01-06 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_estatus_producto_id_variante_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='id_variante',
        ),
    ]
