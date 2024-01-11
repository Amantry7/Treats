from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Settings(models.Model):
    image_title = models.ImageField(
        upload_to='logo',
        verbose_name='логотип'
    )
    image = models.ImageField(
        upload_to='fons',
        verbose_name='фон'
    )
    fons= models.ImageField(
        upload_to='fonss',
        verbose_name='фон2'
    )
    disc = RichTextField(
        verbose_name='Описание'
    )
    image2= models.ImageField(
        upload_to='disc_image',
        verbose_name='фото'
    )
    instagram = models.URLField(
        verbose_name='Истаграмм url'
    )
    dribble= models.URLField(
        verbose_name='Dribbble url'
    )
    twitter = models.URLField(
        verbose_name='твиттер url'
    )
    youtube = models.URLField(
        verbose_name='ютуб url'
    )
    addres = models.CharField(
        max_length=255,
        verbose_name='адрес'
    )
    gmail= models.EmailField(
        verbose_name='email'
    )
    phone= models.CharField(
        max_length=255,
        verbose_name='номер телефона'
    )
    def __str__(self):
        return self.disc
    class Meta():
        verbose_name='Оснавные настройки'
        verbose_name_plural='Оснавные настройки'
        
class Clients(models.Model):
    
    image = models.ImageField(
        upload_to='clients',
        verbose_name='фото клиента'
    )
    name = models.CharField(
        max_length = 255,
        verbose_name='имя клиента'
    )
    prof = models.CharField(
        max_length=255,
        verbose_name='професия клиента'
    )
    disc = models.TextField(
        verbose_name='описание'
    )
    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзавы'
        
        
class Faq(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='название'
    )
    disc = models.TextField(
        verbose_name='описание'
    )
    def __str__(self):
        return self.title
    class Meta():
        verbose_name='Частый задаваеммый вопрос'
        verbose_name_plural='Частые задаваеммые вопрос'
        
