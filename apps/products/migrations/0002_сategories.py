# Generated by Django 5.0.1 on 2024-01-05 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Сategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='popular_katagori', verbose_name='фото')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
            ],
            options={
                'verbose_name': 'Популярные категори',
                'verbose_name_plural': 'Популярные категори',
            },
        ),
    ]
