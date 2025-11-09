from django.db import models


class ServiceHeader(models.Model):
    title = models.CharField(
        max_length=200,
        default="Service",
        verbose_name="Sarlavha"
    )
    background_image = models.ImageField(
        upload_to='service/backgrounds/',
        verbose_name="Fon rasmi",
        null=True,
        blank=True
    )
    overlay_image = models.ImageField(
        upload_to='service/overlays/',
        blank=True,
        null=True,
        verbose_name="Qatlam rasmi"
    )
    home_link_text = models.CharField(
        max_length=50,
        default="Home",
        verbose_name="Bosh sahifa matni"
    )
    read_more_text = models.CharField(
        max_length=100,
        default="Read More",
        verbose_name="Batafsil tugma matni"
    )

    class Meta:
        verbose_name = "Xizmatlar sahifasi sarlavhasi"
        verbose_name_plural = "Xizmatlar sahifasi sarlavhalari"

    def __str__(self):
        return self.title


class ServiceCategory(models.Model):
    """Xizmatlar kategoriyasi"""
    title = models.CharField(
        max_length=200,
        verbose_name="Kategoriya nomi"
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Slug (URL uchun)"
    )
    icon = models.CharField(
        max_length=100,
        default="tji-service-2",
        verbose_name="Ikonka klassi",
        help_text="Masalan: tji-service-2, tji-briefcase"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Faolmi?"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Tartib"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Yaratilgan vaqti"
    )

    class Meta:
        verbose_name = "Xizmat kategoriyasi"
        verbose_name_plural = "Xizmat kategoriyalari"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class Service(models.Model):
    """Xizmatlar modeli"""
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='services',
        verbose_name="Kategoriya"
    )
    title = models.CharField(
        max_length=300,
        verbose_name="Sarlavha"
    )
    description = models.TextField(null=True, blank=True)
    background_image = models.ImageField(
        upload_to='service/backgrounds/',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Slug (URL uchun)"
    )
    icon = models.CharField(
        max_length=100,
        default="tji-service-2",
        verbose_name="Ikonka klassi",
        help_text="Masalan: tji-service-2, tji-briefcase"
    )
    short_description = models.TextField(
        max_length=500,
        verbose_name="Qisqa tavsif"
    )
    full_description = models.TextField(
        verbose_name="To'liq tavsif"
    )
    image = models.ImageField(
        upload_to='services/',
        blank=True,
        null=True,
        verbose_name="Xizmat rasmi"
    )
    animation_delay = models.CharField(
        max_length=10,
        default=".3s",
        verbose_name="Animatsiya kechikishi"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Faolmi?"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Tartib"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Yaratilgan vaqti"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="O'zgartirilgan vaqti"
    )

    class Meta:
        verbose_name = "Xizmat"
        verbose_name_plural = "Xizmatlar"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title