from django.contrib import admin
from apps.core.models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display  = ('id', 'name')
    search_fields = ['id', 'name']
    readonly_fields = ('created', 'updated')
