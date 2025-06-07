from django.contrib import admin
from . models import CustomUser
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')  # Columns to show


admin.site.register(CustomUser, CustomUserAdmin)
    
