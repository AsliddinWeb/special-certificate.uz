from django.contrib import admin
from unfold.admin import ModelAdmin

# ============================================
# TRANSLATION IMPORT
# ============================================
from modeltranslation.admin import TabbedTranslationAdmin
import apps.services_app.translation  # ← QOSHILDI

from .models import ServiceHeader, ServiceCategory, Service


@admin.register(ServiceHeader)
class ServiceHeaderAdmin(TabbedTranslationAdmin, ModelAdmin):
    list_display = ('title', 'home_link_text', 'read_more_text')
    search_fields = ('title',)

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'home_link_text', 'read_more_text')
        }),
        ('Rasmlar', {
            'fields': ('background_image', 'overlay_image')
        }),
    )


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(TabbedTranslationAdmin, ModelAdmin):
    list_display = ('title', 'slug', 'icon', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'slug')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'slug', 'icon')
        }),
        ('Sozlamalar', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(Service)
class ServiceAdmin(TabbedTranslationAdmin, ModelAdmin):
    list_display = ('title', 'category', 'slug', 'order', 'is_active')
    list_filter = ('is_active', 'category', 'created_at')
    search_fields = ('title', 'slug', 'short_description')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('category', 'title', 'slug', 'icon')
        }),
        ('Tafsilotlar', {
            'fields': ('description', 'short_description', 'full_description', 'image', 'background_image')
        }),
        ('Sozlamalar', {
            'fields': ('animation_delay', 'order', 'is_active')
        }),
        ('Vaqt ma\'lumotlari', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')