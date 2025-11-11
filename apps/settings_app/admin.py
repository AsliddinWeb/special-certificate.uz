from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline

# ============================================
# TRANSLATION IMPORT
# ============================================
from modeltranslation.admin import TabbedTranslationAdmin
import apps.settings_app.translation  # ← QOSHILDI

from .models import (
    HeaderSettings, MenuItem,
    FooterSettings, FooterColumn, FooterLink, Newsletter
)


class MenuItemInline(TabularInline):
    model = MenuItem
    extra = 1
    fields = ('title', 'url', 'parent', 'icon', 'order', 'is_active', 'is_mega_menu')


@admin.register(HeaderSettings)
class HeaderSettingsAdmin(TabbedTranslationAdmin, ModelAdmin):  # ← TabbedTranslationAdmin qo'shildi
    list_display = ('phone', 'email', 'is_active', 'updated_at')
    list_filter = ('is_active', 'search_enabled')
    search_fields = ('phone', 'email', 'address')
    inlines = [MenuItemInline]

    fieldsets = (
        ('Logo', {
            'fields': ('logo', 'mobile_logo')
        }),
        ('Kontakt Ma\'lumotlari', {
            'fields': ('phone', 'email', 'address')
        }),
        ('E\'lon', {
            'fields': ('announcement_text', 'announcement_link', 'announcement_active')
        }),
        ('Ijtimoiy Tarmoqlar', {
            'fields': ('facebook_url', 'instagram_url', 'twitter_url', 'linkedin_url', 'telegram_url')
        }),
        ('Qo\'shimcha Sozlamalar', {
            'fields': ('search_enabled', 'is_active')
        }),
    )


@admin.register(MenuItem)
class MenuItemAdmin(TabbedTranslationAdmin, ModelAdmin):  # ← TabbedTranslationAdmin qo'shildi
    list_display = ('title', 'url', 'parent', 'order', 'is_active', 'is_mega_menu')
    list_filter = ('is_active', 'is_mega_menu', 'header_settings')
    search_fields = ('title', 'url')
    list_editable = ('order', 'is_active')


class FooterLinkInline(TabularInline):
    model = FooterLink
    extra = 1
    fields = ('title', 'url', 'badge_text', 'order', 'is_active', 'open_new_tab')


class FooterColumnInline(StackedInline):
    model = FooterColumn
    extra = 1
    fields = ('title', 'order', 'is_active')
    show_change_link = True


@admin.register(FooterSettings)
class FooterSettingsAdmin(TabbedTranslationAdmin, ModelAdmin):  # ← TabbedTranslationAdmin qo'shildi
    list_display = ('phone', 'email', 'is_active', 'newsletter_enabled', 'updated_at')
    list_filter = ('is_active', 'newsletter_enabled', 'show_awards', 'show_social_links')
    search_fields = ('phone', 'email', 'address', 'description')
    inlines = [FooterColumnInline]

    fieldsets = (
        ('Logo va Tavsif', {
            'fields': ('logo', 'description')
        }),
        ('Kontakt Ma\'lumotlari', {
            'fields': ('address', 'phone', 'email', 'working_hours')
        }),
        ('Ijtimoiy Tarmoqlar', {
            'fields': ('facebook_url', 'instagram_url', 'twitter_url', 'linkedin_url', 'telegram_url')
        }),
        ('Newsletter', {
            'fields': ('newsletter_title', 'newsletter_enabled')
        }),
        ('Copyright', {
            'fields': ('copyright_text', 'copyright_link')
        }),
        ('Award Logolar', {
            'fields': ('award_logo_1', 'award_logo_2', 'show_awards')
        }),
        ('Qo\'shimcha Sozlamalar', {
            'fields': ('show_social_links', 'is_active')
        }),
    )


@admin.register(FooterColumn)
class FooterColumnAdmin(TabbedTranslationAdmin, ModelAdmin):  # ← TabbedTranslationAdmin qo'shildi
    list_display = ('title', 'footer_settings', 'order', 'is_active')
    list_filter = ('is_active', 'footer_settings')
    search_fields = ('title',)
    list_editable = ('order', 'is_active')
    inlines = [FooterLinkInline]


@admin.register(FooterLink)
class FooterLinkAdmin(TabbedTranslationAdmin, ModelAdmin):  # ← TabbedTranslationAdmin qo'shildi
    list_display = ('title', 'column', 'url', 'badge_text', 'order', 'is_active')
    list_filter = ('is_active', 'open_new_tab', 'column')
    search_fields = ('title', 'url')
    list_editable = ('order', 'is_active')


@admin.register(Newsletter)
class NewsletterAdmin(ModelAdmin):  # ← Bu yerda translation kerak emas
    list_display = ('email', 'agreed_to_terms', 'is_active', 'subscribed_at')
    list_filter = ('is_active', 'agreed_to_terms', 'subscribed_at')
    search_fields = ('email',)
    readonly_fields = ('subscribed_at',)
    date_hierarchy = 'subscribed_at'

    actions = ['activate_subscribers', 'deactivate_subscribers']

    def activate_subscribers(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} ta obunachi faollashtirildi.')

    activate_subscribers.short_description = 'Tanlangan obunachlarni faollashtirish'

    def deactivate_subscribers(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} ta obunachi o\'chirildi.')

    deactivate_subscribers.short_description = 'Tanlangan obunachlarni o\'chirish'