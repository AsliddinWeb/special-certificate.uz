from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns  # ← Qo'shing
from django.conf import settings
from django.conf.urls.static import static

# Tilsiz URL'lar (til prefixi olmaydi)
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # ← Til almashtirish uchun
]

# Til prefiksli URL'lar
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),

    # Home
    path('', include('apps.main_app.urls')),

    # Settings
    path('settings/', include('apps.settings_app.urls')),

    # News
    path('news/', include('apps.news_app.urls')),

    # Services
    path('services/', include('apps.services_app.urls')),
)

# Media va Static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)