from django.apps import AppConfig


class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.main_app'
    verbose_name = 'Asosiy sahifa'

    # ← YANGI: Translation ni manual import qilish
    def ready(self):
        try:
            import apps.main_app.translation  # noqa
        except ImportError:
            pass
