from django.db import models

# Create your models here.
class RecProduct(models.Model):
    image = models.ImageField(
        upload_to='rec_product',
        verbose_name='фото продукта'
    )
    disc = models.TextField(
        verbose_name='описание'
        )
    price = models.CharField(
        max_length=255,
        verbose_name='цена'
    )
    def __str__(self):
        return self.disc
    class Meta():
        verbose_name='Рекамендованая Продукт'
        verbose_name_plural='Рекамендованые Продукты'
class Сategories(models.Model):
    image = models.ImageField(
        upload_to='popular_katagori',
        verbose_name='фото'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='название'
    )
    class Meta():
        verbose_name= 'Популярные категори'
        verbose_name_plural='Популярные категори'
class ProductAll(models.Model):
    title = models.CharField(
        max_length= 255,
        verbose_name='Название'
        )
    image = models.ImageField(
        upload_to='product_all',
        verbose_name='фото'
    )
    price = models.CharField(
        max_length=255,
        verbose_name='цена'
    )
    def __str__(self):
        return self.title
    class Meta():
        verbose_name='Все продукты'
        verbose_name_plural='Все продукты'
        
class MilkShake(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='milk_shake', verbose_name='Фото')
    price = models.CharField(max_length=255, verbose_name='Цена')
    disc = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Молочный коктель'
        verbose_name_plural = 'Молочные коктели'



class FructJuice(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='fruct_juice/', verbose_name='Фото')
    price = models.CharField(max_length=255, verbose_name='Цена')
    disc = models.TextField(verbose_name='описание')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фруктовый коктель'
        verbose_name_plural = 'Фруктовые коктели'


class IceCreame(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='ice_creame', verbose_name='Фото')
    price = models.CharField(max_length=255, verbose_name='Цена')
    disc = models.TextField(verbose_name='описание')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженые'
        
class Cake(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='cake', verbose_name='Фото')
    price = models.CharField(max_length=255, verbose_name='Цена')
    disc = models.TextField(verbose_name='описание')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты'
        
class Baking(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='baking', verbose_name='Фото')
    price = models.CharField(max_length=255, verbose_name='Цена')
    disc = models.TextField(verbose_name='описание')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Выпычка'
        verbose_name_plural = 'Выпычка'
        
class Cofe(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='cofe', verbose_name='Фото')
    price = models.CharField(max_length=255, verbose_name='Цена')
    disc = models.TextField(verbose_name='описание')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кофе'
        verbose_name_plural = 'кофе'
class PriceChange(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    image= models.ImageField(
        upload_to='price_change/',
        verbose_name='фото'
    )
    disc = models.TextField(
        verbose_name='описание'
    )
    new_price= models.CharField(
        max_length=255,
        verbose_name='новая цена'
    )
    old_price= models.CharField(
        max_length=255,
        verbose_name='старая цена'
    )
    def __str__(self):
        return self.title
    class Meta():
        verbose_name = 'Обнавление цен'
        verbose_name_plural = 'Обнавление цен'
                
        
class CartItem(models.Model):
    product_type_choices = [
        ('ice_cream', 'Мороженое'),
        ('cake', 'Торт'),
        ('baking', 'Выпечка'),
        ('coffee', 'Кофе'),
    ]

    product_type = models.CharField(
        max_length=20,
        choices=product_type_choices,
        verbose_name='Тип продукта'
    )
    product_id = models.PositiveIntegerField(verbose_name='ID продукта')
    quantity = models.PositiveIntegerField(default=1)

    def get_product(self):
        if self.product_type == 'ice_cream':
            return IceCreame.objects.get(pk=self.product_id)
        elif self.product_type == 'cake':
            return Cake.objects.get(pk=self.product_id)
        elif self.product_type == 'baking':
            return Baking.objects.get(pk=self.product_id)
        elif self.product_type == 'coffee':
            return Cofe.objects.get(pk=self.product_id)
        else:
            return None

    def __str__(self):
        product = self.get_product()
        return f"{self.quantity} x {product.title} ({self.product_type})"
    
    def get_product(self):
        if self.product_type == 'ice_cream':
            return IceCreame.objects.get(pk=self.product_id)
        elif self.product_type == 'cake':
            return Cake.objects.get(pk=self.product_id)
        elif self.product_type == 'baking':
            return Baking.objects.get(pk=self.product_id)
        elif self.product_type == 'coffee':
            return Cofe.objects.get(pk=self.product_id)

    def get_total_price(self):
        if self.product_type == 'some_type' and hasattr(self, 'product') and self.product and hasattr(self.product, 'price'):
            return self.quantity * self.product.price
        # Обработка других случаев, если необходимо
        return 0  # Или любое другое значение по умолчанию
