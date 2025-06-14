from django.contrib import admin
from . models import CustomUser,Product,Category
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')  # Columns to show


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name' )
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','price' )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
