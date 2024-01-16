# admin.py
from django.contrib import admin
from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'brand', 'category', 'price', 'stock', 'thumbnail', 'created_at', 'updated_at']

    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)
