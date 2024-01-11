from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Settings,Clients, Faq
from apps.secondary.models import Blog, Gellery, About, Comment,Post
from apps.products.models import RecProduct,Сategories,ProductAll, FructJuice,MilkShake,IceCreame, PriceChange,Cake, Baking, Cofe
# Register your models here.
class ProductAllFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title','price')
    search_fields = ('title', 'price')
    
admin.site.register(Settings)
admin.site.register(Clients)
admin.site.register(RecProduct)
admin.site.register(Сategories)
admin.site.register(FructJuice, ProductAllFilterAdmin)
admin.site.register(MilkShake, ProductAllFilterAdmin)
admin.site.register(IceCreame, ProductAllFilterAdmin)
admin.site.register(ProductAll, ProductAllFilterAdmin)
admin.site.register(PriceChange)
admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Baking)
admin.site.register(About)
admin.site.register(Faq)
admin.site.register(Cofe)
admin.site.register(Cake)
admin.site.register(Comment)
admin.site.register(Gellery)
admin.site.unregister(User)
admin.site.unregister(Group)
