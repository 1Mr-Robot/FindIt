from django.contrib import admin
from .models import *

@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('category', 'created', 'modified')
    search_fields = ('category',)
    date_hierarchy = 'created'

@admin.register(ItemColor)
class ItemColorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('color', 'created', 'modified')
    search_fields = ('color',)
    date_hierarchy = 'created'

@admin.register(CampusZone)
class CampusZoneAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('zone', 'is_active', 'created', 'modified')
    search_fields = ('zone',)
    list_filter = ['is_active',]
    date_hierarchy = 'created'

@admin.register(ItemStatus)
class ItemStatusAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('status', 'created', 'modified')
    search_fields = ('status',)
    date_hierarchy = 'created'

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('name', 'category', 'zone', 'found_date', 'status', 'creator_user')
    search_fields = ('name', 'category', 'zone',)
    list_filter = ['category', 'zone', 'found_date', 'status', 'created']
    date_hierarchy = 'created'

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('item', 'user', 'receipt_code', 'resolved', 'created')
    search_fields = ('item', 'user', 'receipt_code',)
    list_filter = ['resolved']
    date_hierarchy = 'created'