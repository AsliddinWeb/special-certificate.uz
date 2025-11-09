# apps/pages_app/translation.py

from modeltranslation.translator import register, TranslationOptions
from .models import (
    AboutPageTitle, TeamSection, TeamMember,
    ContactHeader, ContactInfo, ContactItem, ContactItemDetail,
    ContactFormSettings, CtaSection
)


# ============================================
# 1. ABOUT PAGE TITLE
# ============================================
@register(AboutPageTitle)
class AboutPageTitleTranslationOptions(TranslationOptions):
    fields = (
        'title_about',
        'title_home',
        'client_text',
    )


# ============================================
# 2. TEAM SECTION
# ============================================
@register(TeamSection)
class TeamSectionTranslationOptions(TranslationOptions):
    fields = (
        'sub_title',
        'main_title',
    )


# ============================================
# 3. TEAM MEMBER
# ============================================
@register(TeamMember)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = (
        'full_name',
        'designation',
    )


# ============================================
# 4. CONTACT HEADER
# ============================================
@register(ContactHeader)
class ContactHeaderTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'home_link_text',
    )


# ============================================
# 5. CONTACT INFO
# ============================================
@register(ContactInfo)
class ContactInfoTranslationOptions(TranslationOptions):
    fields = (
        'subtitle',
        'title',
        'title_highlight',
    )


# ============================================
# 6. CONTACT ITEM
# ============================================
@register(ContactItem)
class ContactItemTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )


# ============================================
# 7. CONTACT ITEM DETAIL
# ============================================
@register(ContactItemDetail)
class ContactItemDetailTranslationOptions(TranslationOptions):
    fields = ('display_text',)


# ============================================
# 8. CONTACT FORM SETTINGS
# ============================================
@register(ContactFormSettings)
class ContactFormSettingsTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'full_name_label',
        'email_label',
        'phone_label',
        'message_label',
        'submit_button_text',
        'success_message',
        'error_message',
    )


# ============================================
# 9. CTA SECTION
# ============================================
@register(CtaSection)
class CtaSectionTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'button_text',
    )