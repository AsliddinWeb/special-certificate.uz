from django.shortcuts import render

from .models import (BannerSection, ClientLogo, ChooseSectionHeader, ChooseCard, AboutSection,
                     TopServiceSectionHeader, TopService, MarqueeItem, CertificateSectionHeader, CertificateCard,
                     NewsSectionHeader, FaqHeader, FaqItem
    )

from apps.news_app.models import News, NewsStaticTexts


def home_page(request):
    """Home page view"""
    banner = BannerSection.objects.filter(is_active=True).first()
    client_logos = ClientLogo.objects.filter(is_active=True)
    choose_header = ChooseSectionHeader.objects.filter(is_active=True).first()
    choose_cards = ChooseCard.objects.filter(is_active=True)
    about_section = AboutSection.objects.filter(is_active=True).first()
    service_header = TopServiceSectionHeader.objects.filter(is_active=True).first()
    services = TopService.objects.filter(is_active=True)
    marquee_items = MarqueeItem.objects.filter(is_active=True)
    certificate_header = CertificateSectionHeader.objects.filter(is_active=True).first()
    certificate_cards = CertificateCard.objects.filter(is_active=True)
    news_header = NewsSectionHeader.objects.filter(is_active=True).first()
    news_static_texts = NewsStaticTexts.objects.all()
    news = News.objects.filter(is_active=True)[:3]
    faq_header = FaqHeader.objects.filter(is_active=True).first()
    faq_items = FaqItem.objects.filter(is_active=True)

    context = {
        'banner': banner,
        'client_logos': client_logos,
        'choose_header': choose_header,
        'choose_cards': choose_cards,
        'about_section': about_section,
        'service_header': service_header,
        'services': services,
        'marquee_items': marquee_items,
        'certificate_header': certificate_header,
        'certificate_cards': certificate_cards,
        'news_header': news_header,
        'news_static_texts': news_static_texts,
        'news': news,
        'faq_header': faq_header,
        'faq_items': faq_items,
    }

    return render(request, 'home.html', context)




def services_page(request):
    return render(request, 'services.html')

def services_detail_page(request):
    return render(request, 'services_detail.html')


def contact_page(request):
    return render(request, 'contact.html')