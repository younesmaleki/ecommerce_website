from django.contrib import admin

# Register your models here.
from .models import ProductDynamicProperty, ProductCategory, Brand, ProductAttribute, Product, ProductColor, \
    ProductAttributeValue, AttributeCategory


@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['fa_name', 'parent', 'created_at']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['fa_name', 'description']


@admin.register(AttributeCategory)
class AttributeCategoryAdmin(admin.ModelAdmin):
    list_display = ['fa_name']


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['fa_name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['fa_name', 'toman_price', 'inventory', 'is_active', 'views']


@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ['fa_name']


@admin.register(ProductDynamicProperty)
class ProductDynamicPropertyAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'value']


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = ['product', 'product_attribute', 'value']
