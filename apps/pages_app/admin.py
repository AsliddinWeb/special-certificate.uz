from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline

# ============================================
# TRANSLATION IMPORT
# ============================================
from modeltranslation.admin import TabbedTranslationAdmin
import apps.pages_app.translation  # ← QOSHILDI

from .models import (AboutPageTitle, TeamSection, TeamMember,
                     ContactHeader, ContactInfo, ContactItem, ContactItemDetail, ContactForm,
                     ContactFormSettings, CtaSection
        )


@admin.register(AboutPageTitle)
class AboutPageTitleAdmin(TabbedTranslationAdmin, ModelAdmin):  # ← TabbedTranslationAdmin qo'shildi
    list_display = ['title_home', 'title_about']


@admin.register(TeamSection)
class TeamSectionAdmin(TabbedTranslationAdmin, ModelAdmin):  # ← TabbedTranslationAdmin qo'shildi
    list_display = ['main_title', 'is_active', 'updated_at']
    list_filter = ['is_active']


@admin.register(TeamMember)
class TeamMemberAdmin(TabbedTranslationAdmin, ModelAdmin):  # ← TabbedTranslationAdmin qo'shildi
    list_display = ['full_name', 'designation', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['full_name', 'designation']
    list_editable = ['order', 'is_active']


@admin.register(ContactHeader)
class ContactHeaderAdmin(TabbedTranslationAdmin, ModelAdmin):  # ← TabbedTranslationAdmin qo'shildi
    list_display = ('title', 'home_link_text')
    search_fields = ('title',)

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'home_link_text')
        }),
        ('Rasmlar', {
            'fields': ('background_image', 'overlay_image')
        }),
    )


class ContactItemDetailInline(admin.TabularInline):
    model = ContactItemDetail
    extra = 1
    fields = ('link_type', 'link_value', 'display_text', 'is_active', 'order')


class ContactItemInline(StackedInline):
    model = ContactItem
    extra = 1
    fields = ('icon', 'title', 'description', 'animation_delay', 'order')
    show_change_link = True


@admin.register(ContactInfo)
class ContactInfoAdmin(TabbedTranslationAdmin, ModelAdmin):  # ← TabbedTranslationAdmin qo'shildi
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')
    inlines = [ContactItemInline]

    fieldsets = (
        ('Sarlavha ma\'lumotlari', {
            'fields': ('subtitle', 'title', 'title_highlight')
        }),
    )


@admin.register(ContactItem)
class ContactItemAdmin(TabbedTranslationAdmin, ModelAdmin):  # ← TabbedTranslationAdmin qo'shildi
    list_display = ('title', 'icon', 'contact_info', 'order')
    list_filter = ('icon', 'contact_info')
    search_fields = ('title', 'description')
    list_editable = ('order',)
    inlines = [ContactItemDetailInline]

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('contact_info', 'icon', 'title', 'description')
        }),
        ('Qo\'shimcha sozlamalar', {
            'fields': ('animation_delay', 'order')
        }),
    )


@admin.register(ContactItemDetail)
class ContactItemDetailAdmin(TabbedTranslationAdmin, ModelAdmin):  # ← TabbedTranslationAdmin qo'shildi
    list_display = ('display_text', 'link_type', 'contact_item', 'is_active', 'order')
    list_filter = ('link_type', 'is_active')
    search_fields = ('display_text', 'link_value')
    list_editable = ('order', 'is_active')

    fieldsets = (
        ('Havola ma\'lumotlari', {
            'fields': ('contact_item', 'link_type', 'link_value', 'display_text')
        }),
        ('Sozlamalar', {
            'fields': ('is_active', 'order')
        }),
    )


@admin.register(ContactForm)
class ContactFormAdmin(ModelAdmin):  # ← Bu yerda translation kerak emas
    list_display = ('full_name', 'email', 'phone', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('full_name', 'email', 'phone', 'subject', 'message')
    list_editable = ('is_read',)
    readonly_fields = ('full_name', 'email', 'phone', 'subject', 'message', 'created_at')
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Shaxsiy ma\'lumotlar', {
            'fields': ('full_name', 'email', 'phone')
        }),
        ('Xabar ma\'lumotlari', {
            'fields': ('subject', 'message')
        }),
        ('Holat', {
            'fields': ('is_read', 'created_at')
        }),
    )


@admin.register(ContactFormSettings)
class ContactFormSettingsAdmin(TabbedTranslationAdmin, ModelAdmin):  # ← TabbedTranslationAdmin qo'shildi
    list_display = ('title',)

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'map_url')
        }),
        ('Forma maydonlari nomlari', {
            'fields': ('full_name_label', 'email_label', 'phone_label', 'message_label', 'submit_button_text')
        }),
        ('Xabarlar', {
            'fields': ('success_message', 'error_message')
        }),
        ('Animatsiya sozlamalari', {
            'fields': ('animation_delay', 'map_animation_delay')
        }),
    )


@admin.register(CtaSection)
class CtaSectionAdmin(TabbedTranslationAdmin, ModelAdmin):  # ← TabbedTranslationAdmin qo'shildi
    list_display = ('title', 'button_text')
    search_fields = ('title', 'button_text')

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'background_image')
        }),
        ('Tugma sozlamalari', {
            'fields': ('button_text', 'button_link')
        }),
        ('Qo\'shimcha sozlamalar', {
            'fields': ('animation_delay',)
        }),
    )