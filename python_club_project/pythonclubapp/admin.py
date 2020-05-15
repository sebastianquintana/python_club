from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ProductType, Product, Review

#register the models.
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Review)