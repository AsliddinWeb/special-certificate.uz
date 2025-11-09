from django.shortcuts import render, redirect

from django.contrib import messages

from apps.main_app.models import ChooseSectionHeader, ChooseCard, AboutSection, ClientLogo, FaqHeader, FaqItem
from .models import (AboutPageTitle, TeamSection, TeamMember, ContactHeader, ContactInfo,
                     ContactForm, ContactFormSettings, CtaSection
            )


def about_page(request):
    about_page_title = AboutPageTitle.objects.last()
    choose_header = ChooseSectionHeader.objects.filter(is_active=True).first()
    choose_cards = ChooseCard.objects.filter(is_active=True)
    about_section = AboutSection.objects.filter(is_active=True).first()
    client_logos = ClientLogo.objects.filter(is_active=True)
    team_section = TeamSection.objects.filter(is_active=True).first()
    team_members = TeamMember.objects.filter(is_active=True)
    faq_header = FaqHeader.objects.filter(is_active=True).first()
    faq_items = FaqItem.objects.filter(is_active=True)

    ctx = {
        'about_page_title': about_page_title,
        'choose_header': choose_header,
        'choose_cards': choose_cards,
        'about_section': about_section,
        'client_logos': client_logos,
        'team_section': team_section,
        'team_members': team_members,
        'faq_header': faq_header,
        'faq_items': faq_items,
    }
    return render(request, 'about.html', ctx)


def contact_page(request):
    contact_header = ContactHeader.objects.last()
    contact_info = ContactInfo.objects.prefetch_related(
        'items__details'
    ).last()
    contact_form_settings = ContactFormSettings.objects.last()
    cta_section = CtaSection.objects.last()

    if request.method == 'POST':
        full_name = request.POST.get('cfName')
        email = request.POST.get('cfEmail')
        phone = request.POST.get('cfPhone')
        message = request.POST.get('cfMessage')

        if full_name and email and phone and message:
            ContactForm.objects.create(
                full_name=full_name,
                email=email,
                phone=phone,
                message=message
            )
            messages.success(request, contact_form_settings.success_message)
            return redirect('contact')
        else:
            messages.error(request, contact_form_settings.error_message)

    ctx = {
        'contact_header': contact_header,
        'contact_info': contact_info,
        'contact_form_settings': contact_form_settings,
        'cta_section': cta_section,
    }
    return render(request, 'contact.html', ctx)


