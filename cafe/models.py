from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    opened_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class BranchInfo(models.Model):
    branch = models.OneToOneField(Branch, on_delete=models.CASCADE)
    manager_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Info for {self.branch.name}"


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField(default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    branches = models.ManyToManyField(Branch)

    def __str__(self):
        return self.name
# Create your models here.
