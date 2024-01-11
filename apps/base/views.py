from django.shortcuts import render,get_object_or_404, redirect
from .models import Settings, Clients,Faq
from apps.secondary.models import Blog,Gellery,About, Comment, Post
from apps.telegram.views import get_text
from apps.contact.models import Reservation, FaqContact , Contact
from django.http import HttpResponse
from apps.products.models import RecProduct, Сategories, ProductAll,FructJuice,IceCreame,MilkShake, PriceChange,Cake, Baking, Cofe, CartItem
# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    categories = Сategories.objects.all()
    rec_product = RecProduct.objects.latest('id')
    product_all = ProductAll.objects.all()
    milk_shakes = MilkShake.objects.all()
    fruct_juices = FructJuice.objects.all()
    ice_creams = IceCreame.objects.all()
    price_change = PriceChange.objects.all()
    clients = Clients.objects.all()
    blog = Blog.objects.all()
    gallery = Gellery.objects.all()
    all_products = list(milk_shakes) + list(fruct_juices) + list(ice_creams)

    return render(request, "base/index-5.html", locals())
def blog_detail(request, blog_id):
    recent_blog = get_object_or_404(Blog, id=blog_id)
    сlients = Clients.objects.all()

    return render(request, 'blog-details.html', locals())

def about(request):
    blog = Blog.objects.all()
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    comment = Comment.objects.all()
    gallery = Gellery.objects.all()
    return render(request, 'about.html', locals())
def menu(request):   
    blog = Blog.objects.all()
    cakes = Cake.objects.all()
    gallery = Gellery.objects.all()
    milk_shakes = MilkShake.objects.all()
    ice_creams = IceCreame.objects.all()
    baking = Baking.objects.all()
    all_disert = list(baking)+ list(cakes) + list(ice_creams)
    cofe = Cofe.objects.all()
    fruct_juices = FructJuice.objects.all()
    all_drinc = list(milk_shakes)+ list(cofe) + list(fruct_juices)
    all_product = list(all_disert)+ list(all_drinc)
    settings = Settings.objects.latest('id')
    return render(request, 'menu1.html', locals())
    
def blog(request):
    blog = Blog.objects.all()
    post = Post.objects.all()
    gallery = Gellery.objects.all()
    settings = Settings.objects.latest('id')    
    return render(request, 'blogs.html', locals())

def contact(request):
    blog = Blog.objects.all()
    settings = Settings.objects.latest('id')   
    gallery = Gellery.objects.all() 
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contacts = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        
        get_text(f"""
оставлена Обратная связь 
Имя: {name}
Почта {email}
Обьект {subject}
Сообщение {message}"""
        )
    return render(request, 'contact.html', locals())    

def reservation(request):
    blog = Blog.objects.all()
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    gallery = Gellery.objects.all() 
    comment = Comment.objects.all()
    if request.method == "POST":
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        person = request.POST.get('person')  # Убедитесь, что 'person' передается в запросе
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')

        # Проверяем, что peQ    S qs     dqswrson не None или пустая строка перед созданием экземпляра Reservation
        if person is not None and person != '':
            new_reservation = Reservation.objects.create(name=name, email=email, person=person, phone=phone, date=date, time=time, message=message)
            get_text(f"""
                Оставлена бронь:
                Имя: {name}
                Email: {email}
                Людей: {person}
                Номер: {phone}
                Дата: {date}
                Время: {time}
                Сообщение: {message}
            """)
    return render(request, 'reservation.html', locals())

def faq(request):
    blog = Blog.objects.all()
    faq = Faq.objects.all()
    settings = Settings.objects.latest('id')
    gallery = Gellery.objects.all() 
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        new_reservation = FaqContact.objects.create(name=name, email=email, subject=subject, message=message)
        get_text(
            f'''
            задан вопрос 
            имя: {name}
            email: {email},
            sibject: {subject}
            вопрос: {message}'''
        )
    return render(request, 'faq.html', locals())

def shop(request):
    settings = Settings.objects.latest('id')
    blog = Blog.objects.all()
    cakes = Cake.objects.all()
    gallery = Gellery.objects.all()
    milk_shakes = MilkShake.objects.all()
    ice_creams = IceCreame.objects.all()
    baking = Baking.objects.all()
    cofe = Cofe.objects.all()
    fruct_juices = FructJuice.objects.all()
    
    all_product = list(fruct_juices)+ list(cofe) + list(baking) + list(ice_creams) + list(milk_shakes) + list(cakes)
    return render(request, 'shop.html', locals())

def add_to_cart(request, product_type, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item, created = CartItem.objects.get_or_create(
            product_type=product_type,
            product_id=product_id,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()
            
        print(f"Item {product_type} - {product_id} added to cart with quantity {quantity}")

    return redirect('view_cart') 

def view_cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.get_total_price() for item in cart_items)
    settings = Settings.objects.latest('id')
    blog = Blog.objects.all()
    cakes = Cake.objects.all()
    gallery = Gellery.objects.all()
    milk_shakes = MilkShake.objects.all()
    ice_creams = IceCreame.objects.all()
    baking = Baking.objects.all()
    cofe = Cofe.objects.all()
    fruct_juices = FructJuice.objects.all()
    
    all_product = list(fruct_juices)+ list(cofe) + list(baking) + list(ice_creams) + list(milk_shakes) + list(cakes)
    return render(request, 'cart.html', locals())
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')