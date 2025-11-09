from django.urls import path

from .views import home_page

from apps.pages_app.views import about_page, contact_page

urlpatterns = [
    # Home
    path('', home_page, name='home_page'),

    # About
    path('about/', about_page, name='about_page'),

    # Contact
    path('contact/', contact_page, name='contact_page'),
]
