# Generated by Django 5.0.1 on 2024-01-06 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0002_blog_delete_clients'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Блог', 'verbose_name_plural': 'Блог'},
        ),
    ]
