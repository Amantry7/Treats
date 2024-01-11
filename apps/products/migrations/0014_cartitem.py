# Generated by Django 5.0.1 on 2024-01-10 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_cofe'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(choices=[('ice_cream', 'Мороженое'), ('cake', 'Торт'), ('baking', 'Выпечка'), ('coffee', 'Кофе')], max_length=20, verbose_name='Тип продукта')),
                ('product_id', models.PositiveIntegerField(verbose_name='ID продукта')),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]