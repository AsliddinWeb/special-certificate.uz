# apps/news_app/translation.py

from modeltranslation.translator import register, TranslationOptions
from .models import NewsCategory, News, NewsHeader, NewsStaticTexts


# ============================================
# 1. NEWS CATEGORY
# ============================================
@register(NewsCategory)
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)
    # Slug har bir tilda alohida bo'lishi kerak
    # Agar xohlasangiz slug ni ham qo'shing:
    # fields = ('title', 'slug')


# ============================================
# 2. NEWS
# ============================================
@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'short_description',
        'content',
    )
    # Agar slug ham kerak bo'lsa:
    # fields = ('title', 'slug', 'short_description', 'content')


# ============================================
# 3. NEWS HEADER
# ============================================
@register(NewsHeader)
class NewsHeaderTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'home_link_text',
    )


# ============================================
# 4. NEWS STATIC TEXTS
# ============================================
@register(NewsStaticTexts)
class NewsStaticTextsTranslationOptions(TranslationOptions):
    fields = (
        'search_text',
        'latest_news',
        'categories',
        'read_more_text',
    )