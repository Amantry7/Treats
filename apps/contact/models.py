from django.db import models

# Create your models here.
class Reservation(models.Model):
    name= models.CharField(
        max_length=255,
        verbose_name='имя'
    )
    email = models.EmailField(
        verbose_name='почта'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='номер'
    )
    person = models.CharField(
        max_length=255,
        verbose_name='количесва людей'
    )
    date = models.DateField(
        verbose_name='дата'
    )
    time = models.CharField(
        max_length=255,
        verbose_name ='время'
    )
    message = models.TextField(
        verbose_name='сообщение'
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Бронирования'
        verbose_name_plural='Бронирование'
        
class FaqContact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='имя'
    )
    email = models.EmailField(
        verbose_name='почта'
    )
    subject= models.CharField(
        max_length=255,
        verbose_name='обьект'
    )
    message = models.TextField(
        verbose_name = 'сообщение'
    )
    def __str__(self):
        return self.name 
    class Meta:
        verbose_name ='Вопрос'
        verbose_name_plural ='Вопросы'
        
        
class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='имя'
    )
    email = models.EmailField(
        verbose_name='Почто'
    )
    subject = models.CharField(
        max_length=255,
        verbose_name='обькт'
    )
    message = models.TextField(
        verbose_name='Сообщение'
    )
    def __str__(self):
        return self.name 
    class Meta:
        verbose_name ='Запросы о связи'
        verbose_name_plural ='Запросы о свяязи'