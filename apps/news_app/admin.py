from django.contrib import admin
from .models import NewsCategory, News, NewsHeader, NewsStaticTexts

from unfold.admin import ModelAdmin


@admin.register(NewsCategory)
class NewsCategoryAdmin(ModelAdmin):
    list_display = ("title", "slug", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-created_at",)
    list_per_page = 20

    fieldsets = (
        ("Asosiy ma'lumotlar", {
            "fields": ("title", "slug", "is_active")
        }),
        ("Vaqt ma'lumotlari", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )
    readonly_fields = ("created_at", "updated_at")

    class Meta:
        verbose_name = "Yangilik kategoriyasi"
        verbose_name_plural = "Yangilik kategoriyalari"


@admin.register(News)
class NewsAdmin(ModelAdmin):
    list_display = ("title", "category", "slug", "views", "is_active", "created_at")
    list_filter = ("category", "is_active", "created_at")
    search_fields = ("title", "short_description", "author")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-created_at",)
    list_per_page = 20
    readonly_fields = ("views", "created_at", "updated_at")

    fieldsets = (
        ("Asosiy ma'lumotlar", {
            "fields": ("title", "slug", "category", "image", "short_description", "content")
        }),
        ("Qo‘shimcha ma'lumotlar", {
            "fields": ("author", "views", "is_active")
        }),
        ("Vaqt ma'lumotlari", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"


@admin.register(NewsHeader)
class NewsHeaderAdmin(ModelAdmin):
    list_display = ('title', 'home_link_text')
    search_fields = ('title',)

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'home_link_text')
        }),
        ('Rasmlar', {
            'fields': ('background_image', 'overlay_image')
        }),
    )


@admin.register(NewsStaticTexts)
class NewsStaticTextsAdmin(ModelAdmin):
    list_display = ('search_text', 'latest_news', 'categories')

    fieldsets = (
        ('Static matnlar', {
            'fields': ('search_text', 'latest_news', 'categories', 'read_more_text')
        }),
    )

    def has_add_permission(self, request):
        # Faqat bitta yozuv bo'lishi uchun
        if self.model.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        # O'chirishni cheklash
        return False
