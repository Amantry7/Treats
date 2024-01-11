from django.db import models

class Blog(models.Model):
    image = models.ImageField(
        upload_to='blog',
        verbose_name='фото'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='название'
    )
    disc = models.TextField(
        verbose_name='описание'
    )
    create_at = models.DateTimeField(
        auto_now_add=True, null= True
        )
    def __str__(self):
        return self.title
    class Meta():
        verbose_name = "Блог"
        verbose_name_plural = "Блог"
        
class Gellery(models.Model):
    image = models.ImageField(
        upload_to='gellery',
        verbose_name='фото'
    )
    intagram = models.URLField(
        verbose_name =  'url истаграм'
    )

    class Meta():
        verbose_name = "Галлерея",
        verbose_name_plural = "Галлерии"
        
class About(models.Model):
    image = models.ImageField(
        upload_to='about/',
        verbose_name='фото'
    )
    disc1 = models.TextField(
        verbose_name='описание для о нас'
    )
    exp = models.CharField(
        max_length=255,
        verbose_name='годы опыты'
    )
    disc2 = models.TextField(
        verbose_name = 'описание о клентов'
    )
    image2= models.ImageField(
        upload_to='about_cliets',
        verbose_name='фото для клиентов'
    )
    def __str__(self):
        return self.disc1
    class Meta():
        verbose_name='О нас'
        verbose_name_plural='О нас'
        
class Comment(models.Model):
    image = models.ImageField(
        upload_to='comment',
        verbose_name='фото'
    )
    name= models.CharField(
        max_length=255,
        verbose_name='имя'
    )
    prof = models.CharField(
        max_length=255,
        verbose_name = 'професия'
    )
    disc = models.TextField(
        verbose_name='описание'
    )
    def __str__(self):
        return self.name
    class Meta():
        verbose_name = 'Коммент',
        verbose_name_plural= 'Комменты'
        
        
class Post(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    create_at = models.DateTimeField(
        auto_now_add=True, null= True
        )
    disc = models.TextField(
        verbose_name='Описание'
    )
    category = models.CharField(
        max_length = 255,
        verbose_name='категория'
    )
    image = models.ImageField(
        upload_to='kategori',
        verbose_name = 'фото'
    )
    made_public = models.CharField(
        max_length=255,
        verbose_name='кто опубликовал'
    )
    def __str__(self):
        return self.title
    class Meta():
        verbose_name ='Пост'
        verbose_name_plural = 'Посты'
