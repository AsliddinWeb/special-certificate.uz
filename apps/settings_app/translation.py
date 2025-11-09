# apps/settings_app/translation.py

from modeltranslation.translator import register, TranslationOptions
from .models import (
    HeaderSettings, MenuItem,
    FooterSettings, FooterColumn, FooterLink
)


# ============================================
# 1. HEADER SETTINGS
# ============================================
@register(HeaderSettings)
class HeaderSettingsTranslationOptions(TranslationOptions):
    fields = (
        'address',
        'announcement_text',
    )


# ============================================
# 2. MENU ITEM
# ============================================
@register(MenuItem)
class MenuItemTranslationOptions(TranslationOptions):
    fields = ('title',)
    # URL ham har xil tilda bo'lishi kerak bo'lsa:
    # fields = ('title', 'url')


# ============================================
# 3. FOOTER SETTINGS
# ============================================
@register(FooterSettings)
class FooterSettingsTranslationOptions(TranslationOptions):
    fields = (
        'description',
        'address',
        'working_hours',
        'newsletter_title',
        'copyright_text',
    )


# ============================================
# 4. FOOTER COLUMN
# ============================================
@register(FooterColumn)
class FooterColumnTranslationOptions(TranslationOptions):
    fields = ('title',)


# ============================================
# 5. FOOTER LINK
# ============================================
@register(FooterLink)
class FooterLinkTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'badge_text',
    )