from django.db import models


class NewsCategory(models.Model):
    """Yangiliklar kategoriyasi"""

    title = models.CharField(
        max_length=200,
        verbose_name="Kategoriya nomi"
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Slug (URL uchun)"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Faolmi?"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Yaratilgan vaqti"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="O‘zgartirilgan vaqti"
    )

    class Meta:
        verbose_name = "Yangilik kategoriyasi"
        verbose_name_plural = "Yangilik kategoriyalari"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class News(models.Model):
    """Yangiliklar modeli"""

    category = models.ForeignKey(
        NewsCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='news',
        verbose_name="Kategoriya"
    )
    title = models.CharField(
        max_length=300,
        verbose_name="Sarlavha"
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Slug (URL uchun)"
    )
    image = models.ImageField(
        upload_to='news_images/',
        verbose_name="Yangilik rasmi"
    )
    short_description = models.TextField(
        max_length=500,
        verbose_name="Qisqa tavsif"
    )
    content = models.TextField(
        verbose_name="To‘liq matn"
    )
    author = models.CharField(
        max_length=150,
        default="Admin",
        verbose_name="Muallif"
    )
    views = models.PositiveIntegerField(
        default=0,
        verbose_name="Ko‘rishlar soni"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Faolmi?"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Yaratilgan vaqti"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="O‘zgartirilgan vaqti"
    )

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class NewsHeader(models.Model):
    title = models.CharField(
        max_length=200,
        default="Blog Right Sidebar",
        verbose_name="Sarlavha"
    )
    background_image = models.ImageField(
        upload_to='news/backgrounds/',
        verbose_name="Fon rasmi"
    )
    overlay_image = models.ImageField(
        upload_to='news/overlays/',
        blank=True,
        null=True,
        verbose_name="Qatlam rasmi"
    )
    home_link_text = models.CharField(
        max_length=50,
        default="Home",
        verbose_name="Bosh sahifa matni"
    )

    class Meta:
        verbose_name = "Yangiliklar sahifasi sarlavhasi"
        verbose_name_plural = "Yangiliklar sahifasi sarlavhalari"

    def __str__(self):
        return self.title

class NewsStaticTexts(models.Model):
    search_text = models.CharField(max_length=200, verbose_name="Qidiruv matni")
    latest_news = models.CharField(max_length=200, verbose_name="Oxirgi yangiliklar matni")
    categories = models.CharField(max_length=200, verbose_name="Kategoriyalar matni")
    read_more_text = models.CharField(max_length=200, verbose_name="Oxirgi yangiliklar matni", null=True, blank=True)

    class Meta:
        verbose_name = "Yangiliklar sahifasi static matn"
        verbose_name_plural = "Yangiliklar sahifasi static matnlar"
