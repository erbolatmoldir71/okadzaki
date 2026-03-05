from django.shortcuts import render

# "База данных" пока в виде списка (для практической так можно)
PRODUCTS = [
    {"id": 1, "slug": "okadzaki-set", "name": "Сет №1 - 40 штук + пицца Маргарита в подарок + 1л Coca-cola в подарок", "price": 10500, "in_stock": True,
     "description": "", "image": "webapp/image/set1.png"},
    {"id": 2, "slug": "okadzaki-set", "name": "Сет №2 - 40 штук + 1л Coca-cola в подарок", "price": 10000, "in_stock": True,
     "description": "", "image": "webapp/image/set2.png"},
    {"id": 3, "slug": "okadzaki-set", "name": "Сет №3 - 32 штук + пицца Пеперони и 1л Coca-colaa в подарок", "price": 10000, "in_stock": True,
     "description": "", "image": "webapp/image/set3.png"},
    {"id": 4, "slug": "okadzaki-set", "name": "Сет №4 - 32 штук + 1л Coca-cola в подарок", "price": 8800, "in_stock": True,
     "description": "", "image": "webapp/image/set4.png"},
    {"id": 5, "slug": "okadzaki-set", "name": "Сет Фудзи -  24 штук + 1л Coca-cola в подарок", "price": 8000, "in_stock": True,
     "description": "", "image": "webapp/image/set5.png"},
    {"id": 6, "slug": "okadzaki-set", "name": "Сет Оптимальный -  24 штук + пицца Маргарита и 1л Coca-cola в подарок", "price": 8500, "in_stock": True,
     "description": "", "image": "webapp/image/set6.png"},
    {"id": 7, "slug": "okadzaki-set", "name": "Сет Роберто де Ниро -  32 штук + пицца Пепперони в подарок", "price": 9500, "in_stock": True,
     "description": "", "image": "webapp/image/set7.png"},
]

CATEGORIES = [
    {"slug": "sushi", "title": "Суши"},
    {"slug": "rolls", "title": "Роллы"},
    {"slug": "sets", "title": "Сеты"},
]

def home(request):
    return render(request, "home.html", {
        "title": "Главная",
        "categories": CATEGORIES,
        "products": PRODUCTS[:7],
    })

def about(request):
    return render(request, "about.html", {
        "title": "О нас",
        "shop_name": "Okadzaki",
        "city": "Almaty",
        "is_open": True,
    })

def catalog(request):
    return render(request, "catalog.html", {
        "title": "Каталог",
        "products": PRODUCTS,
        "categories": CATEGORIES,
    })

def product_by_id(request, id):
    product = next((p for p in PRODUCTS if p["id"] == id), None)
    return render(request, "product_detail.html", {
        "title": "Товар",
        "product": product,
    })

def category_page(request, slug):
    category = next((c for c in CATEGORIES if c["slug"] == slug), None)
    return render(request, "category.html", {
        "title": "Категория",
        "category": category,
        "products": PRODUCTS,
    })

from .models import Product

def menu_db(request):
    products = Product.objects.all()
    return render(request, "menu_db.html", {
        "title": "Меню из базы",
        "products": products
    })