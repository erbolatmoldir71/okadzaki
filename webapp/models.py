from django.db import models

class Category(models.Model):
    # CharField
    name = models.CharField(max_length=100)
    # CharField + unique (slug для URL)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    # CharField
    name = models.CharField(max_length=100, unique=True)
    # BooleanField + default (требование "default")
    is_allergen = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    # ForeignKey (One-to-Many): Category -> Product
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    # CharField
    name = models.CharField(max_length=120)
    # TextField + blank=True (уместно)
    description = models.TextField(blank=True)

    # DecimalField
    price = models.DecimalField(max_digits=8, decimal_places=2)

    # IntegerField + default
    grams = models.IntegerField(default=250)

    # BooleanField + default
    in_stock = models.BooleanField(default=True)

    # DateTimeField + auto_now_add=True (требование "auto_now_add")
    created_at = models.DateTimeField(auto_now_add=True)

    # ManyToManyField (Many-to-Many): Product <-> Ingredient
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name="products",
        blank=True
    )

    def __str__(self):
        return self.name


class ProductDetail(models.Model):
    # OneToOneField (One-to-One): Product -> ProductDetail
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name="detail"
    )

    # IntegerField
    calories = models.IntegerField(default=0)

    # CharField + null/blank (уместно, может быть неизвестно)
    spicy_level = models.CharField(max_length=20, null=True, blank=True)

    # BooleanField + default
    chef_choice = models.BooleanField(default=False)

    def __str__(self):
        return f"Detail: {self.product.name}"