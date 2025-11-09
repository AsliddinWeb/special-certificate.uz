# apps/settings_app/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Newsletter


def newsletter_subscribe(request):
    """Newsletter obuna bo'lish"""
    if request.method == 'POST':
        email = request.POST.get('email')
        agreed = request.POST.get('agree')

        if not email:
            messages.error(request, 'Email manzilni kiriting!')
            return redirect(request.META.get('HTTP_REFERER', '/'))

        if not agreed:
            messages.error(request, 'Shartlarga rozilik berishingiz kerak!')
            return redirect(request.META.get('HTTP_REFERER', '/'))

        # Email mavjudligini tekshirish
        if Newsletter.objects.filter(email=email).exists():
            messages.warning(request, 'Bu email allaqachon ro\'yxatdan o\'tgan!')
            return redirect(request.META.get('HTTP_REFERER', '/'))

        # Yangi obunachi qo'shish
        Newsletter.objects.create(
            email=email,
            agreed_to_terms=True,
            is_active=True
        )

        messages.success(request, 'Muvaffaqiyatli obuna bo\'ldingiz!')
        return redirect(request.META.get('HTTP_REFERER', '/'))

    return redirect('/')


def newsletter_subscribe_ajax(request):
    """AJAX orqali newsletter obuna bo'lish"""
    if request.method == 'POST':
        email = request.POST.get('email')
        agreed = request.POST.get('agree')

        if not email:
            return JsonResponse({
                'success': False,
                'message': 'Email manzilni kiriting!'
            })

        if not agreed:
            return JsonResponse({
                'success': False,
                'message': 'Shartlarga rozilik berishingiz kerak!'
            })

        # Email mavjudligini tekshirish
        if Newsletter.objects.filter(email=email).exists():
            return JsonResponse({
                'success': False,
                'message': 'Bu email allaqachon ro\'yxatdan o\'tgan!'
            })

        # Yangi obunachi qo'shish
        Newsletter.objects.create(
            email=email,
            agreed_to_terms=True,
            is_active=True
        )

        return JsonResponse({
            'success': True,
            'message': 'Muvaffaqiyatli obuna bo\'ldingiz!'
        })

    return JsonResponse({
        'success': False,
        'message': 'Noto\'g\'ri so\'rov!'
    })
