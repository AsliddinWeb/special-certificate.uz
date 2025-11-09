from django.urls import path

from . import views

urlpatterns = [
    path('<slug:category_slug>/', views.services_page, name='services_page'),
    path('<slug:category_slug>/<slug:service_slug>/', views.service_detail, name='service_detail'),
]
