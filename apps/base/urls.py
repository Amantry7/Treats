from django.urls import path
from . import views
urlpatterns = [
        path('', views.index, name='index'),
        path('about/', views.about, name='about'),
        path('menu/', views.menu, name='menu'),
        path('blog/', views.blog, name='blog'),
        path('contact/', views.contact, name='contact'),
        path('blog_detail/<int:blog_id>/', views.blog_detail, name='blog_detail'),
        path('reservation', views.reservation, name='reservation'),
        path('faq/', views.faq, name='faq'),
        path('shop/', views.shop, name='shop'),
    path('add_to_cart/<str:product_type>/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
        path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),

        path('cart/', views.view_cart, name='view_cart'),
    ]
