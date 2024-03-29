# Generated by Django 5.0.1 on 2024-01-08 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0006_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('disc', models.TextField(verbose_name='Описание')),
                ('category', models.CharField(max_length=255, verbose_name='категория')),
                ('image', models.ImageField(upload_to='kategori', verbose_name='фото')),
                ('made_public', models.CharField(max_length=255, verbose_name='кто опубликовал')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
