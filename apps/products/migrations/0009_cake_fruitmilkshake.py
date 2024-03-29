# Generated by Django 5.0.1 on 2024-01-08 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_fructjuice_disc_icecreame_disc_milkshake_disc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='cake', verbose_name='Фото')),
                ('price', models.CharField(max_length=255, verbose_name='Цена')),
                ('disc', models.TextField(verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='FruitMilkshake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='fruits_milk_shake', verbose_name='Фото')),
                ('price', models.CharField(max_length=255, verbose_name='Цена')),
                ('disc', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Фруктовый милкшейк',
                'verbose_name_plural': 'Фруктовые милкшейки',
            },
        ),
    ]
