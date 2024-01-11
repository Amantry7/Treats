# Generated by Django 5.0.1 on 2024-01-06 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productall'),
    ]

    operations = [
        migrations.CreateModel(
            name='FructJuice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='fruct_juice', verbose_name='фото')),
                ('price', models.CharField(max_length=255, verbose_name='цена')),
            ],
            options={
                'verbose_name': 'Фруктовый коктель',
                'verbose_name_plural': 'Фруктовые коктели',
            },
        ),
        migrations.CreateModel(
            name='IceCreame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='ice_creame', verbose_name='фото')),
                ('price', models.CharField(max_length=255, verbose_name='цена')),
            ],
            options={
                'verbose_name': 'Мороженое',
                'verbose_name_plural': 'Мороженые',
            },
        ),
        migrations.CreateModel(
            name='MilkShake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='milk_shake', verbose_name='фото')),
                ('price', models.CharField(max_length=255, verbose_name='цена')),
            ],
            options={
                'verbose_name': 'Молочный коктель',
                'verbose_name_plural': 'Молочные продукты',
            },
        ),
    ]