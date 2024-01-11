# Generated by Django 5.0.1 on 2024-01-08 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0004_gellery'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/', verbose_name='фото')),
                ('disc1', models.TextField(verbose_name='описание для о нас')),
                ('exp', models.CharField(max_length=255, verbose_name='годы опыты')),
                ('disc2', models.TextField(verbose_name='описание о клентов')),
                ('image2', models.ImageField(upload_to='about_cliets', verbose_name='фото для клиентов')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
    ]