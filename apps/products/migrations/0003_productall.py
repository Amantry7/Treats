# Generated by Django 5.0.1 on 2024-01-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_сategories'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='product_all', verbose_name='фото')),
                ('price', models.CharField(max_length=255, verbose_name='цена')),
            ],
            options={
                'verbose_name': 'Все продукты',
                'verbose_name_plural': 'Все продукты',
            },
        ),
    ]