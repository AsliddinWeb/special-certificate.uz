from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin, TabularInline

from django.utils.html import format_html
from .models import (BannerSection, ClientLogo, ChooseSectionHeader, ChooseCard, AboutSection, AboutProgress,
                     TopServiceSectionHeader, TopService, MarqueeItem, CertificateSectionHeader, CertificateCard,
                     NewsSectionHeader, FaqHeader, FaqItem
    )

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(BannerSection)
class BannerSectionAdmin(ModelAdmin):
    list_display = [
        'get_title',
        'director_name',
        'phone_number',
        'is_active',
        'created_at',
        'updated_at'
    ]

    list_filter = [
        'is_active',
    ]

    search_fields = [
        'main_title_line1',
        'main_title_line2',
        'director_name',
        'phone_number',
        'sub_title_text'
    ]

    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': (
                'is_active',
                ('sub_title_icon', 'sub_title_text'),
            )
        }),
        ('Sarlavha', {
            'fields': (
                'main_title_line1',
                'main_title_line2',
                'main_title_small',
            )
        }),
        ('Tugma sozlamalari', {
            'fields': (
                'button_text',
                'button_link',
                'button_icon',
            )
        }),
        ('Telefon ma\'lumotlari', {
            'fields': (
                'phone_number',
                'phone_icon',
            )
        }),
        ('Rasmlar', {
            'fields': (
                'hero_image',
                'growth_image',
                'bg_shape_1',
                'bg_shape_2',
            )
        }),
        ('Marquee matnlar', {
            'fields': (
                'marquee_text1',
                'marquee_text2',
            )
        }),
        ('Direktor ma\'lumotlari', {
            'fields': (
                'director_name',
                'director_designation',
            )
        }),
        ('Scroll tugmasi', {
            'fields': (
                'scroll_text',
                'scroll_link',
                'scroll_icon',
            )
        }),
        ('Vaqt ma\'lumotlari', {
            'fields': (
                'created_at',
                'updated_at',
            ),
            'classes': ('collapse',)
        }),
    )

    def get_title(self, obj):
        """Sarlavhani qisqacha ko'rsatish"""
        return f"{obj.main_title_line1}{obj.main_title_line2}"

    get_title.short_description = 'Sarlavha'


@admin.register(ClientLogo)
class ClientLogoAdmin(ModelAdmin):
    list_display = [
        'name',
        'order',
        'is_active',
        'logo_preview',
        'created_at'
    ]

    list_filter = [
        'is_active',
    ]

    search_fields = [
        'name',
        'website_url'
    ]

    list_editable = ['order', 'is_active']

    readonly_fields = ['logo_preview', 'created_at', 'updated_at']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': (
                'name',
                'logo',
                'logo_preview',
                'order',
                'is_active',
            )
        }),
        ('Qo\'shimcha', {
            'fields': (
                'website_url',
            )
        }),
        ('Vaqt ma\'lumotlari', {
            'fields': (
                'created_at',
                'updated_at',
            ),
            'classes': ('collapse',)
        }),
    )

    def logo_preview(self, obj):
        """Logo previewni ko'rsatish"""
        if obj.logo:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px;" />',
                obj.logo.url
            )
        return "-"

    logo_preview.short_description = 'Logo ko\'rinishi'


@admin.register(ChooseSectionHeader)
class ChooseSectionHeaderAdmin(ModelAdmin):
    list_display = [
        'main_title',
        'sub_title',
        'is_active',
        'created_at'
    ]

    list_filter = [
        'is_active',
    ]

    search_fields = [
        'main_title',
        'sub_title'
    ]

    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Sarlavhalar', {
            'fields': (
                'sub_title_icon',
                'sub_title',
                'main_title',
                'is_active',
            )
        }),
        ('Vaqt ma\'lumotlari', {
            'fields': (
                'created_at',
                'updated_at',
            ),
            'classes': ('collapse',)
        }),
    )


@admin.register(ChooseCard)
class ChooseCardAdmin(ModelAdmin):
    list_display = [
        'title',
        'order',
        'is_active',
        'icon_preview',
        'created_at'
    ]

    list_filter = [
        'is_active',
    ]

    search_fields = [
        'title',
        'description'
    ]

    list_editable = ['order', 'is_active']

    readonly_fields = ['icon_preview', 'created_at', 'updated_at']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': (
                'icon',
                'icon_preview',
                'title',
                'description',
                'order',
                'is_active',
            )
        }),
        ('Tugma sozlamalari', {
            'fields': (
                'button_text',
                'button_link',
                'button_icon',
            )
        }),
        ('Vaqt ma\'lumotlari', {
            'fields': (
                'created_at',
                'updated_at',
            ),
            'classes': ('collapse',)
        }),
    )

    def icon_preview(self, obj):
        """Ikon previewni ko'rsatish"""
        if obj.icon:
            return format_html(
                '<i class="{}" style="font-size: 24px;"></i>',
                obj.icon
            )
        return "-"

    icon_preview.short_description = 'Ikon ko\'rinishi'


class AboutProgressInline(TabularInline):
    model = AboutProgress
    extra = 1
    fields = ['title', 'percent', 'order', 'is_active']
    ordering = ['order']


@admin.register(AboutSection)
class AboutSectionAdmin(ModelAdmin):
    list_display = [
        'sub_title',
        'mission_title',
        'vision_title',
        'is_active',
        'created_at'
    ]

    list_filter = [
        'is_active',
    ]

    search_fields = [
        'sub_title',
        'main_title',
        'mission_title',
        'vision_title'
    ]

    readonly_fields = ['image_preview', 'created_at', 'updated_at']

    inlines = [AboutProgressInline]

    fieldsets = (
        ('Rasm', {
            'fields': (
                'main_image',
                'image_preview',
            )
        }),
        ('Progress box', {
            'fields': (
                'progress_box_title',
            )
        }),
        ('Sarlavhalar', {
            'fields': (
                'sub_title_icon',
                'sub_title',
                'main_title',
            )
        }),
        ('Maqsadimiz (Mission)', {
            'fields': (
                'mission_title',
                'mission_description',
                'mission_item1',
                'mission_item2',
                'mission_item3',
            )
        }),
        ('Qarashlarimiz (Vision)', {
            'fields': (
                'vision_title',
                'vision_description',
                'vision_item1',
                'vision_item2',
                'vision_item3',
            )
        }),
        ('Tugma sozlamalari', {
            'fields': (
                'button_text',
                'button_link',
                'button_icon',
            )
        }),
        ('Fon shakllari', {
            'fields': (
                'bg_shape_1',
                'bg_shape_2',
            )
        }),
        ('Status va vaqt', {
            'fields': (
                'is_active',
                'created_at',
                'updated_at',
            ),
            'classes': ('collapse',)
        }),
    )

    def image_preview(self, obj):
        """Rasm previewni ko'rsatish"""
        if obj.main_image:
            return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 300px;" />',
                obj.main_image.url
            )
        return "-"

    image_preview.short_description = 'Rasm ko\'rinishi'


@admin.register(AboutProgress)
class AboutProgressAdmin(ModelAdmin):
    list_display = [
        'title',
        'percent',
        'about_section',
        'order',
        'is_active',
        'progress_bar_preview'
    ]

    list_filter = [
        'is_active',
        'about_section'
    ]

    search_fields = [
        'title'
    ]

    list_editable = ['percent', 'order', 'is_active']

    def progress_bar_preview(self, obj):
        """Progress bar previewni ko'rsatish"""
        return format_html(
            '<div style="width: 100px; height: 20px; background: #e0e0e0; border-radius: 10px; overflow: hidden;">'
            '<div style="width: {}%; height: 100%; background: #4caf50;"></div>'
            '</div>',
            obj.percent
        )

    progress_bar_preview.short_description = 'Progress ko\'rinishi'


@admin.register(TopServiceSectionHeader)
class ServiceSectionHeaderAdmin(ModelAdmin):
    list_display = [
        'main_title',
        'sub_title',
        'button_text',
        'is_active',
        'created_at'
    ]

    list_filter = [
        'is_active',
    ]

    search_fields = [
        'main_title',
        'sub_title',
        'button_text'
    ]

    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Sarlavhalar', {
            'fields': (
                'sub_title_icon',
                'sub_title',
                'main_title',
                'is_active',
            )
        }),
        ('Tugma sozlamalari', {
            'fields': (
                'button_text',
                'button_link',
                'button_icon',
            )
        }),
        ('Vaqt ma\'lumotlari', {
            'fields': (
                'created_at',
                'updated_at',
            ),
            'classes': ('collapse',)
        }),
    )


@admin.register(TopService)
class ServiceAdmin(ModelAdmin):
    list_display = [
        'title',
        'order',
        'is_active',
        'icon_preview',
        'image_preview',
        'created_at'
    ]

    list_filter = [
        'is_active',
    ]

    search_fields = [
        'title',
        'description'
    ]

    list_editable = ['order', 'is_active']

    readonly_fields = ['icon_preview', 'image_preview', 'created_at', 'updated_at']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': (
                'icon',
                'icon_preview',
                'title',
                'description',
                'detail_link',
                'order',
                'is_active',
            )
        }),
        ('Fon rasmi', {
            'fields': (
                'background_image',
                'image_preview',
            )
        }),
        ('Vaqt ma\'lumotlari', {
            'fields': (
                'created_at',
                'updated_at',
            ),
            'classes': ('collapse',)
        }),
    )

    def icon_preview(self, obj):
        """Ikon previewni ko'rsatish"""
        if obj.icon:
            return format_html(
                '<i class="{}" style="font-size: 24px;"></i>',
                obj.icon
            )
        return "-"

    icon_preview.short_description = 'Ikon ko\'rinishi'

    def image_preview(self, obj):
        """Rasm previewni ko'rsatish"""
        if obj.background_image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 150px;" />',
                obj.background_image.url
            )
        return "-"

    image_preview.short_description = 'Rasm ko\'rinishi'


@admin.register(MarqueeItem)
class MarqueeItemAdmin(ModelAdmin):
    list_display = (
        'title',
        'order',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_editable = ('order', 'is_active')
    list_filter = ('is_active', )
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at', 'order')
    date_hierarchy = 'created_at'

    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'order', 'is_active')
        }),
        ('Vaqt maʼlumotlari', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at'),
        }),
    )


@admin.register(CertificateCard)
class CertificateCardAdmin(ModelAdmin):
    list_display = ('title', 'header', 'order', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    ordering = ('order',)
    list_editable = ('order', 'is_active')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('header', 'title', 'description', 'image', 'link')
        }),
        ('Qo‘shimcha ma’lumotlar', {
            'fields': ('order', 'is_active', 'created_at', 'updated_at')
        }),
    )


class CertificateCardInline(TabularInline):
    model = CertificateCard
    extra = 1
    fields = ('title', 'description', 'image', 'link', 'order', 'is_active')
    ordering = ('order',)
    show_change_link = True


@admin.register(CertificateSectionHeader)
class CertificateSectionHeaderAdmin(ModelAdmin):
    list_display = ('main_title', 'sub_title', 'button_text', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('main_title', 'sub_title')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [CertificateCardInline]

    fieldsets = (
        ('Asosiy sarlavha ma’lumotlari', {
            'fields': ('sub_title_icon', 'sub_title', 'main_title')
        }),
        ('Tugma sozlamalari', {
            'fields': ('button_text', 'button_link', 'button_icon')
        }),
        ('Holat', {
            'fields': ('is_active', 'created_at', 'updated_at')
        }),
    )


@admin.register(NewsSectionHeader)
class NewsSectionHeaderAdmin(ModelAdmin):
    list_display = ('main_title', 'sub_title', 'is_active',)
    list_filter = ('is_active', )
    search_fields = ('main_title', 'sub_title')
    ordering = ('-created_at',)
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Sarlavha maʼlumotlari', {
            'fields': ('sub_title_icon', 'sub_title', 'main_title')
        }),
        ('Tugma sozlamalari', {
            'fields': ('button_text', 'button_link', 'button_icon')
        }),
        ('Faollik va vaqt', {
            'fields': ('is_active', 'created_at', 'updated_at')
        }),
    )


class FaqItemInline(TabularInline):
    """FAQ bo‘limi uchun inline savol-javoblar"""
    model = FaqItem
    extra = 1
    fields = ('question', 'answer', 'order', 'is_active')
    ordering = ('order',)
    show_change_link = True


@admin.register(FaqHeader)
class FaqHeaderAdmin(ModelAdmin):
    """FAQ sarlavhasi uchun admin"""
    list_display = ('title', 'phone_number', 'is_active', 'created_at')
    list_filter = ('is_active', )
    search_fields = ('title', 'subtitle', 'phone_number')
    inlines = [FaqItemInline]
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('image', 'title', 'subtitle', 'is_active')
        }),
        ("Aloqa ma’lumotlari", {
            'fields': ('call_title', 'phone_number', 'phone_icon')
        }),
        ("Vaqt ma’lumotlari", {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(FaqItem)
class FaqItemAdmin(ModelAdmin):
    """FAQ savol-javob elementlari uchun admin"""
    list_display = ('question', 'header', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'header')
    search_fields = ('question', 'answer')
    ordering = ('order',)
    readonly_fields = ('created_at', 'updated_at')
