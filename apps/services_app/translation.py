# apps/services_app/translation.py

from modeltranslation.translator import register, TranslationOptions
from .models import ServiceHeader, ServiceCategory, Service


# ============================================
# 1. SERVICE HEADER
# ============================================
@register(ServiceHeader)
class ServiceHeaderTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'home_link_text',
        'read_more_text',
    )


# ============================================
# 2. SERVICE CATEGORY
# ============================================
@register(ServiceCategory)
class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)
    # Slug kerak bo'lsa:
    # fields = ('title', 'slug')


# ============================================
# 3. SERVICE
# ============================================
@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
        'short_description',
        'full_description',
    )
    # Slug kerak bo'lsa:
    # fields = ('title', 'slug', 'description', ...)