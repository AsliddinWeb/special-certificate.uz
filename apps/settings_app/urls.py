# apps/settings_app/urls.py

from django.urls import path
from . import views

app_name = 'settings'

urlpatterns = [
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('newsletter/subscribe/ajax/', views.newsletter_subscribe_ajax, name='newsletter_subscribe_ajax'),
]