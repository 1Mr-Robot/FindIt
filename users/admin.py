from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('tuition', 'institutional_email', 'first_name', 'last_name', 'phone', 'is_staff', 'is_active')
    search_fields = ('tuition', 'institutional_email', 'first_name', 'last_name', 'phone')
    list_filter = ('is_staff', 'is_active')
    ordering = ('tuition',)
    date_hierarchy = 'date_joined'
    list_per_page = 50