from django.contrib import admin
from .models import Product, Product_type, Product_detail_type

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'product_detail_type']
    list_display_links = ['id', 'title']

class Product_detail_Admin(admin.ModelAdmin):
    list_display = ['id', 'detail_type', 'product_type']
    list_display_links = ['id', 'detail_type']
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Product_type)
admin.site.register(Product_detail_type, Product_detail_Admin)
