# apps/main_app/translation.py

from modeltranslation.translator import register, TranslationOptions
from .models import (
    BannerSection, ClientLogo, ChooseSectionHeader, ChooseCard,
    AboutSection, AboutProgress, TopServiceSectionHeader, TopService,
    MarqueeItem, CertificateSectionHeader, CertificateCard,
    NewsSectionHeader, FaqHeader, FaqItem
)


# ============================================
# 1. BANNER SECTION
# ============================================
@register(BannerSection)
class BannerSectionTranslationOptions(TranslationOptions):
    fields = (
        'sub_title_text',
        'main_title_line1',
        'main_title_line2',
        'main_title_small',
        'button_text',
        'marquee_text1',
        'marquee_text2',
        'director_name',
        'director_designation',
        'scroll_text',
    )


# ============================================
# 2. CLIENT LOGO
# ============================================
@register(ClientLogo)
class ClientLogoTranslationOptions(TranslationOptions):
    fields = ('name',)


# ============================================
# 3. CHOOSE SECTION HEADER
# ============================================
@register(ChooseSectionHeader)
class ChooseSectionHeaderTranslationOptions(TranslationOptions):
    fields = (
        'sub_title',
        'main_title',
    )


# ============================================
# 4. CHOOSE CARD
# ============================================
@register(ChooseCard)
class ChooseCardTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
        'button_text',
    )


# ============================================
# 5. ABOUT SECTION
# ============================================
@register(AboutSection)
class AboutSectionTranslationOptions(TranslationOptions):
    fields = (
        'progress_box_title',
        'sub_title',
        'main_title',
        'mission_title',
        'mission_description',
        'mission_item1',
        'mission_item2',
        'mission_item3',
        'vision_title',
        'vision_description',
        'vision_item1',
        'vision_item2',
        'vision_item3',
        'button_text',
    )


# ============================================
# 6. ABOUT PROGRESS
# ============================================
@register(AboutProgress)
class AboutProgressTranslationOptions(TranslationOptions):
    fields = ('title',)


# ============================================
# 7. TOP SERVICE SECTION HEADER
# ============================================
@register(TopServiceSectionHeader)
class TopServiceSectionHeaderTranslationOptions(TranslationOptions):
    fields = (
        'sub_title',
        'main_title',
        'button_text',
    )


# ============================================
# 8. TOP SERVICE
# ============================================
@register(TopService)
class TopServiceTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )


# ============================================
# 9. MARQUEE ITEM
# ============================================
@register(MarqueeItem)
class MarqueeItemTranslationOptions(TranslationOptions):
    fields = ('title',)


# ============================================
# 10. CERTIFICATE SECTION HEADER
# ============================================
@register(CertificateSectionHeader)
class CertificateSectionHeaderTranslationOptions(TranslationOptions):
    fields = (
        'sub_title',
        'main_title',
        'button_text',
    )


# ============================================
# 11. CERTIFICATE CARD
# ============================================
@register(CertificateCard)
class CertificateCardTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )


# ============================================
# 12. NEWS SECTION HEADER
# ============================================
@register(NewsSectionHeader)
class NewsSectionHeaderTranslationOptions(TranslationOptions):
    fields = (
        'sub_title',
        'main_title',
        'button_text',
    )


# ============================================
# 13. FAQ HEADER
# ============================================
@register(FaqHeader)
class FaqHeaderTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'subtitle',
        'call_title',
    )


# ============================================
# 14. FAQ ITEM
# ============================================
@register(FaqItem)
class FaqItemTranslationOptions(TranslationOptions):
    fields = (
        'question',
        'answer',
    )