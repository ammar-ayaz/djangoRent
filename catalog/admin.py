from django.contrib import admin

# Register your models here.

from catalog.models import Product, Category 
from catalog.forms import ProductAdminForm 
class ProductAdmin(admin.ModelAdmin): 
     form = ProductAdminForm 
     # sets values for how the admin site lists your products  
     list_display = ('title', 'price', 'old_price', 'created_at', 'updated_at',) 
     list_display_links = ('title',) 
     list_per_page = 50 
     ordering = ['-created_at'] 
     search_fields = ['title', 'description', 'meta_keywords', 'meta_description'] 
     exclude = ('created_at', 'updated_at',) 
     # sets up slug to be generated from product title 
     prepopulated_fields = {'slug' : ('title',)} 

# registers your product model with the admin site 
admin.site.register(Product, ProductAdmin) 

class CategoryAdmin(admin.ModelAdmin): 
     #sets up values for how admin site lists categories 
     list_display = ('title', 'created_at', 'updated_at',) 
     list_display_links = ('title',) 
     list_per_page = 20 
     ordering = ['title'] 
     search_fields = ['title', 'description', 'meta_keywords', 'meta_description'] 
     exclude = ('created_at', 'updated_at',) 
     # sets up slug to be generated from category title 
     prepopulated_fields = {'slug' : ('title',)} 
admin.site.register(Category, CategoryAdmin) 