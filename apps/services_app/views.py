from django.shortcuts import render, get_object_or_404
from .models import ServiceHeader, Service, ServiceCategory
from apps.pages_app.models import CtaSection


def services_page(request, category_slug):
    """Kategoriya bo'yicha xizmatlar"""
    service_header = ServiceHeader.objects.last()
    category = get_object_or_404(ServiceCategory, slug=category_slug, is_active=True)

    services = Service.objects.filter(
        category=category,
        is_active=True
    ).select_related('category')

    categories = ServiceCategory.objects.filter(is_active=True)
    cta_section = CtaSection.objects.last()

    ctx = {
        'service_header': service_header,
        'services': services,
        'categories': categories,
        'selected_category': category,
        'cta_section': cta_section,
    }

    return render(request, 'services/services_list.html', ctx)


def service_detail(request, category_slug, service_slug):
    """Xizmat tafsilotlari"""
    service_header = ServiceHeader.objects.last()
    category = get_object_or_404(ServiceCategory, slug=category_slug, is_active=True)
    service = get_object_or_404(Service, slug=service_slug, category=category, is_active=True)

    # O'xshash xizmatlar (bir xil kategoriyadan)
    related_services = Service.objects.filter(
        category=category,
        is_active=True
    ).exclude(id=service.id)[:3]

    categories = ServiceCategory.objects.filter(is_active=True)
    cta_section = CtaSection.objects.last()

    ctx = {
        'service_header': service_header,
        'service': service,
        'related_services': related_services,
        'categories': categories,
        'selected_category': category,
        'cta_section': cta_section,
    }

    return render(request, 'services/service_detail.html', ctx)