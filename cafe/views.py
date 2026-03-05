from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def menu(request):
    dishes = [
        {
            'name': 'Сет №1',
            'description': '40 шт + пицца Маргарита в подарок и 1л Coca-Cola в подарок',
            'old_price': 21000,
            'price': 10500,
            'image': 'images/set1.png'
        },
        {
            'name': 'Сет №2',
            'description': '40 шт + 1л Coca-Cola в подарок',
            'old_price': 20000,
            'price': 10000,
            'image': 'images/set2.png'
        },
        {
            'name': 'Сет №3',
            'description': '32 шт + пицца Пепперони и 1л Coca-Cola в подарок',
            'old_price': 20000,
            'price': 10000,
            'image': 'images/set3.png'
        },
        {
            'name': 'Сет №4',
            'description': '32 шт + 11л Coca-Cola в подарок',
            'old_price': 17600,
            'price': 8800,
            'image': 'images/set4.png'
        },
        {
            'name': 'Сет "Фудзи" ',
            'description': '24 шт + 1л Coca-Cola в подарок',
            'price': 8000,
            'image': 'images/set5.png'
        },
        {
            'name': 'Сет "Оптимальный"',
            'description': '24 шт + пицца Маргарита и 1л Coca-Cola в подарок',
            'price': 8500,
            'image': 'images/set6.png'
        },
        {
            'name': 'Сет "Роберто де Ниро " ',
            'description': '32 шт + пицца Пепперони в подарок',
            'price': 9500,
            'image': 'images/set7.png'
        }
    ]
    iftar_sets = [
    {
        'name': 'Ифтар Сет №1',
        'description': 'Сырный равен с курицей,Аляска запеченая с курицей,Греческий салат,Дрожжевые булочки- 2шт,Морс-0,3,Финики',
        'price': 7500,
        'image': 'images/iftar1.png'
    },
    {
        'name': 'Ифтар Сет №2',
        'description': 'Куриный суп,Удон с говядиной,Греческий салат,Дрожжевые булочки - 2 шт,Морс - 0,3,Финики',
        'price': 7500,
        'image': 'images/iftar2.png'
    },
    {
        'name': 'Ифтар Сет №3',
        'description': 'Говяжий суп,Курица по-тайски,Греческий салат,Дрожжевые булочки - 2 шт,Морс - 0,3,Финики',
        'price': 7500,
        'image': 'images/iftar3.png'
    }
]

    return render(request, 'menu.html', {
        'dishes': dishes,
        'iftar_sets': iftar_sets
    })


def branches(request):
    cities = [
        {'name': 'Astana', 'count': 15},
        {'name': 'Almaty', 'count': 15},
    ]
    return render(request, 'branches.html', {'cities': cities})

def branch_detail(request, id):
    return render(request, 'branch_detail.html', {'id': id})

def about(request):
    info = {
        'branches_total': 30,
        'astana': 15,
        'almaty': 15,
        'halal': True,
        'kids_zone': True
    }

    return render(request, 'about.html', {'info': info})

from .models import Product

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})