from django.contrib import admin
from src.menu.models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'url', 'named_url')