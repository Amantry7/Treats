# Generated by Django 5.0.1 on 2024-01-06 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_fructjuice_icecreame_milkshake'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='milkshake',
            options={'verbose_name': 'Молочный коктель', 'verbose_name_plural': 'Молочные коктели'},
        ),
        migrations.AddField(
            model_name='fructjuice',
            name='category',
            field=models.CharField(default='fruct_juice', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='icecreame',
            name='category',
            field=models.CharField(default='ice_creame', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='milkshake',
            name='category',
            field=models.CharField(default='milk_shake', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='fructjuice',
            name='image',
            field=models.ImageField(upload_to='fruct_juice', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='fructjuice',
            name='price',
            field=models.CharField(max_length=255, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='icecreame',
            name='image',
            field=models.ImageField(upload_to='ice_creame', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='icecreame',
            name='price',
            field=models.CharField(max_length=255, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='milkshake',
            name='image',
            field=models.ImageField(upload_to='milk_shake', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='milkshake',
            name='price',
            field=models.CharField(max_length=255, verbose_name='Цена'),
        ),
    ]