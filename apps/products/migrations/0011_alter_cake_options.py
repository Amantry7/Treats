# Generated by Django 5.0.1 on 2024-01-08 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_delete_fruitmilkshake'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cake',
            options={'verbose_name': 'Выпычка', 'verbose_name_plural': 'Выпачки'},
        ),
    ]