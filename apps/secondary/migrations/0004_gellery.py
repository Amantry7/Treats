# Generated by Django 5.0.1 on 2024-01-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0003_alter_blog_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gellery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gellery', verbose_name='фото')),
                ('intagram', models.URLField(verbose_name='url истаграм')),
            ],
            options={
                'verbose_name': ('Галлерея',),
                'verbose_name_plural': 'Галлерии',
            },
        ),
    ]