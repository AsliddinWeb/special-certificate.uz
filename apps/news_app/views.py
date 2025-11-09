from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

from .models import News, NewsCategory, NewsHeader, NewsStaticTexts

from apps.pages_app.models import CtaSection


def all_news(request):
    """Barcha yangiliklar ro'yxati"""

    # Header
    news_header = NewsHeader.objects.last()

    # Qidiruv va kategoriya bo'yicha filtrlash
    search_query = request.GET.get('search', '')
    category_slug = request.GET.get('category')

    news_list = News.objects.filter(is_active=True).select_related('category')

    # Qidiruv
    if search_query:
        news_list = news_list.filter(
            Q(title__icontains=search_query) |
            Q(short_description__icontains=search_query) |
            Q(content__icontains=search_query)
        )

    # Kategoriya filtri
    if category_slug:
        news_list = news_list.filter(category__slug=category_slug)

    # Pagination
    paginator = Paginator(news_list, 8)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)

    # Barcha kategoriyalar
    categories = NewsCategory.objects.filter(is_active=True)
    latest_news = News.objects.filter(is_active=True)[:3]

    cta_section = CtaSection.objects.last()
    static_texts = NewsStaticTexts.objects.last()

    ctx = {
        'news_header': news_header,
        'news': news,
        'categories': categories,
        'selected_category': category_slug,
        'search_query': search_query,
        'cta_section': cta_section,
        'static_texts': static_texts,
        'latest_news': latest_news,
    }

    return render(request, 'news/all_news.html', ctx)


def news_detail(request, slug):
    """Yangilik tafsilotlari"""

    news = get_object_or_404(News, slug=slug, is_active=True)

    # Header
    news_header = NewsHeader.objects.last()
    static_texts = NewsStaticTexts.objects.last()

    # Ko'rishlar sonini oshirish
    news.views += 1
    news.save(update_fields=['views'])

    latest_news = News.objects.filter(is_active=True)[:3]
    categories = NewsCategory.objects.filter(is_active=True)
    cta_section = CtaSection.objects.last()

    ctx = {
        'news': news,
        'latest_news': latest_news,

        'news_header': news_header,
        'static_texts': static_texts,
        'categories': categories,
        'cta_section': cta_section,
    }

    return render(request, 'news/news_detail.html', ctx)
