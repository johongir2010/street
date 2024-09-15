from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


# Register your models here.
# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['chat_id', 'lang', 'city', 'name', 'contact']
    list_filter = ['chat_id', 'lang', 'city']
    search_fields = ['chat_id', 'lang', 'city']


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'item', 'count']
    list_filter = ['id', 'user']
    ordering = ['-id']


# admin.site.register(Basket)
admin.site.register(City)
# admin.site.register(Branches)
# admin.site.register(Category)
# admin.site.register(Items)
