from django.db import models


class HeaderSettings(models.Model):
    """Header sozlamalari uchun model"""

    # Logo
    logo = models.ImageField(upload_to='logos/', verbose_name='Logo')
    mobile_logo = models.ImageField(upload_to='logos/', verbose_name='Mobil Logo')

    # Kontakt ma'lumotlari
    phone = models.CharField(max_length=20, verbose_name='Telefon raqami')
    email = models.EmailField(verbose_name='Email manzil')
    address = models.CharField(max_length=255, verbose_name='Manzil')

    # E'lon (Announcement)
    announcement_text = models.CharField(max_length=255, verbose_name='E\'lon matni', blank=True)
    announcement_link = models.URLField(verbose_name='E\'lon havolasi', blank=True)
    announcement_active = models.BooleanField(default=True, verbose_name='E\'lonni ko\'rsatish')

    # Ijtimoiy tarmoqlar
    facebook_url = models.URLField(blank=True, verbose_name='Facebook')
    instagram_url = models.URLField(blank=True, verbose_name='Instagram')
    twitter_url = models.URLField(blank=True, verbose_name='Twitter/X')
    linkedin_url = models.URLField(blank=True, verbose_name='LinkedIn')
    telegram_url = models.URLField(blank=True, verbose_name='Telegram')

    # Qo'shimcha sozlamalar
    search_enabled = models.BooleanField(default=True, verbose_name='Qidiruvni yoqish')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='O\'zgartirilgan sana')
    is_active = models.BooleanField(default=True, verbose_name='Faol')

    class Meta:
        verbose_name = '1. Header Sozlamasi'
        verbose_name_plural = '1. Header Sozlamalari'
        ordering = ['-created_at']

    def __str__(self):
        return f"Header Sozlamasi - {self.phone}"

    def save(self, *args, **kwargs):
        # Faqat bitta faol header sozlamasi bo'lishi kerak
        if self.is_active:
            HeaderSettings.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


class MenuItem(models.Model):
    """Menyu elementlari uchun model"""

    header_settings = models.ForeignKey(
        HeaderSettings,
        on_delete=models.CASCADE,
        related_name='menu_items',
        verbose_name='Header sozlamasi'
    )
    title = models.CharField(max_length=100, verbose_name='Sarlavha')
    url = models.CharField(max_length=255, verbose_name='URL manzil')
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Ota menyu'
    )
    icon = models.CharField(max_length=50, blank=True, verbose_name='Ikon klassi')
    order = models.IntegerField(default=0, verbose_name='Tartib raqami')
    is_active = models.BooleanField(default=True, verbose_name='Faol')
    is_mega_menu = models.BooleanField(default=False, verbose_name='Mega menyu')

    class Meta:
        verbose_name = '2. Menyu'
        verbose_name_plural = '2. Menyular'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class FooterSettings(models.Model):
    """Footer sozlamalari uchun model"""

    # Logo va asosiy ma'lumotlar
    logo = models.ImageField(upload_to='footer_logos/', verbose_name='Footer Logo')
    description = models.TextField(verbose_name='Tavsif', help_text='Footer qismidagi qisqacha tavsif')

    # Kontakt ma'lumotlari
    address = models.CharField(max_length=255, verbose_name='Manzil')
    phone = models.CharField(max_length=20, verbose_name='Telefon raqami')
    email = models.EmailField(verbose_name='Email manzil')
    working_hours = models.CharField(max_length=100, verbose_name='Ish vaqti', default='Du–Ju: 09:00 – 18:00')

    # Ijtimoiy tarmoqlar
    facebook_url = models.URLField(blank=True, verbose_name='Facebook')
    instagram_url = models.URLField(blank=True, verbose_name='Instagram')
    twitter_url = models.URLField(blank=True, verbose_name='Twitter/X')
    linkedin_url = models.URLField(blank=True, verbose_name='LinkedIn')
    telegram_url = models.URLField(blank=True, verbose_name='Telegram')

    # Newsletter sozlamalari
    newsletter_title = models.CharField(max_length=255, verbose_name='Newsletter sarlavhasi',
                                        default='Yangiliklarimizga obuna bo\'ling')
    newsletter_enabled = models.BooleanField(default=True, verbose_name='Newsletter yoqilgan')

    # Copyright
    copyright_text = models.CharField(max_length=255, verbose_name='Copyright matni',
                                      default='Barcha huquqlar himoyalangan.')
    copyright_link = models.URLField(blank=True, verbose_name='Copyright havolasi')

    # Award logos
    award_logo_1 = models.ImageField(upload_to='footer_awards/', blank=True, null=True, verbose_name='Award Logo 1')
    award_logo_2 = models.ImageField(upload_to='footer_awards/', blank=True, null=True, verbose_name='Award Logo 2')

    # Qo'shimcha sozlamalar
    show_awards = models.BooleanField(default=True, verbose_name='Award logolarni ko\'rsatish')
    show_social_links = models.BooleanField(default=True, verbose_name='Ijtimoiy tarmoqlarni ko\'rsatish')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='O\'zgartirilgan sana')
    is_active = models.BooleanField(default=True, verbose_name='Faol')

    class Meta:
        verbose_name = '3. Footer Sozlamasi'
        verbose_name_plural = '3. Footer Sozlamalari'
        ordering = ['-created_at']

    def __str__(self):
        return f"Footer Sozlamasi - {self.phone}"

    def save(self, *args, **kwargs):
        # Faqat bitta faol footer sozlamasi bo'lishi kerak
        if self.is_active:
            FooterSettings.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


class FooterColumn(models.Model):
    """Footer ustunlari uchun model"""

    footer_settings = models.ForeignKey(
        FooterSettings,
        on_delete=models.CASCADE,
        related_name='columns',
        verbose_name='Footer sozlamasi'
    )
    title = models.CharField(max_length=100, verbose_name='Ustun sarlavhasi')
    order = models.IntegerField(default=0, verbose_name='Tartib raqami')
    is_active = models.BooleanField(default=True, verbose_name='Faol')

    class Meta:
        verbose_name = '4. Footer Ustuni'
        verbose_name_plural = '4. Footer Ustunlari'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    """Footer havolalari uchun model"""

    column = models.ForeignKey(
        FooterColumn,
        on_delete=models.CASCADE,
        related_name='links',
        verbose_name='Footer ustuni'
    )
    title = models.CharField(max_length=100, verbose_name='Havola nomi')
    url = models.CharField(max_length=255, verbose_name='URL manzil')
    icon = models.CharField(max_length=50, blank=True, verbose_name='Ikon klassi')
    badge_text = models.CharField(max_length=20, blank=True, verbose_name='Badge matni',
                                  help_text='Masalan: Yangi, Hot')
    order = models.IntegerField(default=0, verbose_name='Tartib raqami')
    is_active = models.BooleanField(default=True, verbose_name='Faol')
    open_new_tab = models.BooleanField(default=False, verbose_name='Yangi oynada ochish')

    class Meta:
        verbose_name = '5. Footer Havolasi'
        verbose_name_plural = '5. Footer Havolalari'
        ordering = ['order', 'title']

    def __str__(self):
        return f"{self.column.title} - {self.title}"


class Newsletter(models.Model):
    """Newsletter obunachilari uchun model"""

    email = models.EmailField(unique=True, verbose_name='Email')
    agreed_to_terms = models.BooleanField(default=False, verbose_name='Shartlarga roziman')
    is_active = models.BooleanField(default=True, verbose_name='Faol')
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name='Obuna sanasi')

    class Meta:
        verbose_name = '6. Newsletter Obunachisi'
        verbose_name_plural = '6. Newsletter Obunachilar'
        ordering = ['-subscribed_at']

    def __str__(self):
        return self.email
