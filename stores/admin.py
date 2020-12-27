from django.contrib import admin
from .models.products import Product
from .models.category import Categorie
from .models.customer import Customer

# Register your models here.
class AdminProduct(admin.ModelAdmin):
	list_display = ['id', 'name', 'category', 'price']

class AdminCategory(admin.ModelAdmin):
	list_display = ['id', 'title', 'subcategory']

admin.site.register(Product, AdminProduct)
admin.site.register(Categorie, AdminCategory)
admin.site.register(Customer)
