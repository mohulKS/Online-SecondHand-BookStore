from django.contrib import admin
from .models.products import Product
from .models.category import Category
from .models.contactform import Contact

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminContact(admin.ModelAdmin):
    list_display = ['name','email','subject','message']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Contact)