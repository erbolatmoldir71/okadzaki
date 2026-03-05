from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("catalog/", views.catalog, name="catalog"),
    path("product/<int:id>/", views.product_by_id, name="product_by_id"),
    path("category/<str:slug>/", views.category_page, name="category_page"),
    path("menu-db/", views.menu_db, name="menu_db"),
]