# apps/settings_app/context_processors.py

from .models import HeaderSettings, MenuItem, FooterSettings, FooterColumn, FooterLink


def header_settings(request):
    """
    Header sozlamalarini barcha sahifalarga uzatish uchun context processor
    """
    try:
        # Faol header sozlamasini olish
        settings = HeaderSettings.objects.filter(is_active=True).first()

        if settings:
            # Asosiy menyu elementlarini olish (parent=None bo'lganlar)
            # prefetch_related bilan barcha sub-menularni ham olish
            main_menu_items = MenuItem.objects.filter(
                header_settings=settings,
                is_active=True,
                parent=None
            ).select_related('header_settings').prefetch_related(
                'children',
                'children__children',  # 3-daraja menyu uchun
                'children__children__children'  # 4-daraja menyu uchun
            ).order_by('order')

            context = {
                'header_settings': settings,
                'main_menu_items': main_menu_items,
                'social_links': {
                    'facebook': settings.facebook_url,
                    'instagram': settings.instagram_url,
                    'twitter': settings.twitter_url,
                    'linkedin': settings.linkedin_url,
                    'telegram': settings.telegram_url,
                },
                'contact_info': {
                    'phone': settings.phone,
                    'email': settings.email,
                    'address': settings.address,
                },
                'announcement': {
                    'text': settings.announcement_text,
                    'link': settings.announcement_link,
                    'active': settings.announcement_active,
                } if settings.announcement_active and settings.announcement_text else None,
            }
        else:
            context = {
                'header_settings': None,
                'main_menu_items': [],
                'social_links': {},
                'contact_info': {},
                'announcement': None,
            }

        return context

    except Exception as e:
        return {
            'header_settings': None,
            'main_menu_items': [],
            'social_links': {},
            'contact_info': {},
            'announcement': None,
        }


def footer_settings(request):
    """
    Footer sozlamalarini barcha sahifalarga uzatish uchun context processor
    """
    try:
        # Faol footer sozlamasini olish
        settings = FooterSettings.objects.filter(is_active=True).first()

        if settings:
            # Footer ustunlarini va ularning havolalarini olish
            footer_columns = FooterColumn.objects.filter(
                footer_settings=settings,
                is_active=True
            ).prefetch_related(
                'links'
            ).order_by('order')

            # Har bir ustun uchun havolalarni filtrlash
            for column in footer_columns:
                column.active_links = column.links.filter(is_active=True).order_by('order')

            context = {
                'footer_settings': settings,
                'footer_columns': footer_columns,
                'footer_social_links': {
                    'facebook': settings.facebook_url,
                    'instagram': settings.instagram_url,
                    'twitter': settings.twitter_url,
                    'linkedin': settings.linkedin_url,
                    'telegram': settings.telegram_url,
                },
                'footer_contact': {
                    'address': settings.address,
                    'phone': settings.phone,
                    'email': settings.email,
                    'working_hours': settings.working_hours,
                },
                'footer_newsletter': {
                    'title': settings.newsletter_title,
                    'enabled': settings.newsletter_enabled,
                } if settings.newsletter_enabled else None,
                'footer_copyright': {
                    'text': settings.copyright_text,
                    'link': settings.copyright_link,
                },
                'footer_awards': {
                    'logo_1': settings.award_logo_1,
                    'logo_2': settings.award_logo_2,
                    'show': settings.show_awards,
                } if settings.show_awards else None,
            }
        else:
            context = {
                'footer_settings': None,
                'footer_columns': [],
                'footer_social_links': {},
                'footer_contact': {},
                'footer_newsletter': None,
                'footer_copyright': {},
                'footer_awards': None,
            }

        return context

    except Exception as e:
        return {
            'footer_settings': None,
            'footer_columns': [],
            'footer_social_links': {},
            'footer_contact': {},
            'footer_newsletter': None,
            'footer_copyright': {},
            'footer_awards': None,
        }


def site_settings(request):
    """
    Umumiy sayt sozlamalari uchun context processor
    """
    from datetime import datetime

    return {
        'site_name': 'Special Certificate',
        'current_year': datetime.now().year,
    }
