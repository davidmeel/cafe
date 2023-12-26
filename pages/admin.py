from django.contrib import admin
from pages.models import *


@admin.register(Mode)
class ModeNameAdmin(admin.ModelAdmin):
    list_display = ['title',  'created_at', 'updated_at']
    search_fields = ['title', 'info']
    list_filter = ['created_at', 'updated_at']


@admin.register(ReservationModel)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['name',  'created_at', 'updated_at']
    search_fields = ['name', 'message']
    list_filter = ['created_at', 'updated_at']



@admin.register(MenuModel)
class MenuModelAdmin(admin.ModelAdmin):
    list_display = ['title',  'price', 'updated_at']
    search_fields = ['title', 'price']
    list_filter = ['created_at', 'updated_at']