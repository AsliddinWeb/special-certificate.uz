from django.db import models

# 1. Banner
class BannerSection(models.Model):
    """Banner bo'limi uchun model"""

    # Asosiy mazmun
    sub_title_icon = models.CharField(
        max_length=50,
        default='tji-box',
        verbose_name='Sub-sarlavha ikona',
        help_text='Font Awesome yoki maxsus ikon klassi'
    )
    sub_title_text = models.CharField(
        max_length=200,
        default='Qarshi shahridagi',
        verbose_name='Sub-sarlavha matni'
    )

    main_title_line1 = models.CharField(
        max_length=100,
        default='Special-',
        verbose_name='Asosiy sarlavha 1-qator'
    )
    main_title_line2 = models.CharField(
        max_length=100,
        default='Certificate',
        verbose_name='Asosiy sarlavha 2-qator'
    )
    main_title_small = models.CharField(
        max_length=100,
        default='labaratoriyasi.',
        verbose_name='Sarlavha kichik matni'
    )

    # Tugmalar
    button_text = models.CharField(
        max_length=100,
        default='Biz Haqimizda',
        verbose_name='Tugma matni'
    )
    button_link = models.CharField(
        max_length=255,
        default='#',
        verbose_name='Tugma havolasi',
        help_text='URL yoki slug'
    )
    button_icon = models.CharField(
        max_length=50,
        default='tji-arrow-right-long',
        verbose_name='Tugma ikona',
        help_text='Font Awesome yoki maxsus ikon klassi'
    )

    # Telefon raqam
    phone_number = models.CharField(
        max_length=20,
        default='+998942025511',
        verbose_name='Telefon raqami'
    )
    phone_icon = models.CharField(
        max_length=50,
        default='tji-phone',
        verbose_name='Telefon ikona'
    )

    # Banner rasmi
    hero_image = models.ImageField(
        upload_to='banner/hero/',
        verbose_name='Asosiy rasm',
        help_text='Banner uchun asosiy rasm'
    )

    # Marquee (harakatlanuvchi) matnlar
    marquee_text1 = models.CharField(
        max_length=50,
        default='Special',
        verbose_name='Marquee matni 1'
    )
    marquee_text2 = models.CharField(
        max_length=50,
        default='Certificate',
        verbose_name='Marquee matni 2'
    )

    # O'sish (growth) rasmi
    growth_image = models.ImageField(
        upload_to='banner/growth/',
        verbose_name='O\'sish rasmi',
        help_text='Growth box uchun rasm'
    )

    # Direktor ma'lumotlari
    director_name = models.CharField(
        max_length=100,
        default='Asliddin Abdujabborov',
        verbose_name='Direktor ismi'
    )
    director_designation = models.CharField(
        max_length=100,
        default='Direktor',
        verbose_name='Direktor lavozimi'
    )

    # Fon shakllari
    bg_shape_1 = models.ImageField(
        upload_to='banner/shapes/',
        verbose_name='Fon shakli 1',
        blank=True,
        null=True
    )
    bg_shape_2 = models.ImageField(
        upload_to='banner/shapes/',
        verbose_name='Fon shakli 2',
        blank=True,
        null=True
    )

    # Scroll tugmasi
    scroll_text = models.CharField(
        max_length=50,
        default='Pastga',
        verbose_name='Scroll tugmasi matni'
    )
    scroll_link = models.CharField(
        max_length=255,
        default='#choose',
        verbose_name='Scroll havolasi'
    )
    scroll_icon = models.CharField(
        max_length=50,
        default='tji-arrow-down-long',
        verbose_name='Scroll ikona'
    )

    # Status va vaqt
    is_active = models.BooleanField(
        default=True,
        verbose_name='Faolmi?',
        help_text='Banner faol yoki faol emasligini belgilaydi'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Yaratilgan vaqti'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='O\'zgartirilgan vaqti'
    )

    class Meta:
        verbose_name = '1. Banner'
        verbose_name_plural = '1. Bannerlar'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.main_title_line1}{self.main_title_line2} - {self.director_name}"

    def get_formatted_phone(self):
        """Telefon raqamini formatlangan ko'rinishda qaytaradi"""
        phone = self.phone_number.replace('+', '').replace(' ', '')
        return f"+{phone[:3]} ({phone[3:5]}) {phone[5:8]}-{phone[8:10]}-{phone[10:]}"

# 2. Partners
class ClientLogo(models.Model):
    """Mijozlar logotipi uchun model"""

    name = models.CharField(
        max_length=200,
        verbose_name='Mijoz nomi',
        help_text='Kompaniya yoki tashkilot nomi'
    )

    logo = models.ImageField(
        upload_to='clients/logos/',
        verbose_name='Logo',
        help_text='Mijoz logotipi (webp formatida tavsiya etiladi)'
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Tartib raqami',
        help_text='Kichik raqam birinchi ko\'rsatiladi'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Faolmi?',
        help_text='Logotip ko\'rsatilsinmi?'
    )

    website_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name='Veb-sayt',
        help_text='Mijozning veb-sayti (ixtiyoriy)'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Qo\'shilgan vaqti'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='O\'zgartirilgan vaqti'
    )

    class Meta:
        verbose_name = '2. Hamkor'
        verbose_name_plural = '2. Hamkorlar'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.name

# 3. Choose title
class ChooseSectionHeader(models.Model):
    """Nega aynan biz? bo'limi sarlavhasi uchun model"""

    sub_title_icon = models.CharField(
        max_length=50,
        default='tji-box',
        verbose_name='Sub-sarlavha ikona',
        help_text='Font Awesome yoki maxsus ikon klassi'
    )

    sub_title = models.CharField(
        max_length=200,
        default='Maxsus-sertifikat',
        verbose_name='Sub-sarlavha'
    )

    main_title = models.CharField(
        max_length=200,
        default='Nega aynan biz?',
        verbose_name='Asosiy sarlavha'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Faolmi?',
        help_text='Bo\'lim sarlavhasi faol yoki nofaol'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Yaratilgan vaqti'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='O\'zgartirilgan vaqti'
    )

    class Meta:
        verbose_name = '3. Afzallik sarlavhasi'
        verbose_name_plural = '3. Afzallik sarlavhalari'
        ordering = ['-created_at']

    def __str__(self):
        return self.main_title

# 3. Choose cards
class ChooseCard(models.Model):
    """Nega aynan biz? kartochkalari uchun model"""

    icon = models.CharField(
        max_length=50,
        verbose_name='Ikona',
        help_text='Font Awesome yoki maxsus ikon klassi (masalan: tji-innovative)'
    )

    title = models.CharField(
        max_length=200,
        verbose_name='Sarlavha'
    )

    description = models.TextField(
        verbose_name='Tavsif',
        help_text='Kartochka matni'
    )

    button_text = models.CharField(
        max_length=100,
        default='Batafsil',
        verbose_name='Tugma matni'
    )

    button_link = models.CharField(
        max_length=255,
        default='#',
        verbose_name='Tugma havolasi',
        help_text='URL yoki slug'
    )

    button_icon = models.CharField(
        max_length=50,
        default='tji-arrow-right-long',
        verbose_name='Tugma ikona'
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Tartib raqami',
        help_text='Kichik raqam birinchi ko\'rsatiladi'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Faolmi?',
        help_text='Kartochka ko\'rsatilsinmi?'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Yaratilgan vaqti'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='O\'zgartirilgan vaqti'
    )

    class Meta:
        verbose_name = '3. Afzalliklar'
        verbose_name_plural = '3. Afzalliklar'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

# 4. About
class AboutSection(models.Model):
    """Biz haqimizda bo'limi uchun model"""

    # Rasm
    main_image = models.ImageField(
        upload_to='about/images/',
        verbose_name='Asosiy rasm',
        help_text='Laboratoriya rasmi'
    )

    # Progress box
    progress_box_title = models.CharField(
        max_length=200,
        default='Ish faoliyatimiz ko\'rsatkichlari',
        verbose_name='Ko\'rsatkichlar sarlavhasi'
    )

    # Sarlavha
    sub_title_icon = models.CharField(
        max_length=50,
        default='tji-lab',
        verbose_name='Sub-sarlavha ikona'
    )

    sub_title = models.CharField(
        max_length=200,
        default='Biz haqimizda',
        verbose_name='Sub-sarlavha'
    )

    main_title = models.TextField(
        default='Qarshi shahridagi ishonchli va xalqaro standartlarga mos sertifikatlash laboratoriyasi.',
        verbose_name='Asosiy sarlavha'
    )

    # Mission box
    mission_title = models.CharField(
        max_length=200,
        default='Bizning maqsadimiz',
        verbose_name='Maqsad sarlavhasi'
    )

    mission_description = models.TextField(
        default='Maxsulot va xizmatlarning sifatini xalqaro standartlarga muvofiq baholab, mijozlarimizga ishonchli sertifikatlar taqdim etish.',
        verbose_name='Maqsad tavsifi'
    )

    mission_item1 = models.CharField(
        max_length=200,
        default='Xalqaro talablar asosida sinov',
        verbose_name='Maqsad 1-bandı'
    )

    mission_item2 = models.CharField(
        max_length=200,
        default='Sifat kafolati',
        verbose_name='Maqsad 2-bandı'
    )

    mission_item3 = models.CharField(
        max_length=200,
        default='Shaffoflik va tezkorlik',
        verbose_name='Maqsad 3-bandı'
    )

    # Vision box
    vision_title = models.CharField(
        max_length=200,
        default='Bizning qarashimiz',
        verbose_name='Qarashlari sarlavhasi'
    )

    vision_description = models.TextField(
        default='O\'zbekiston va mintaqada yetakchi sertifikatlash markaziga aylanish hamda global ishonch qozonish.',
        verbose_name='Qarashlari tavsifi'
    )

    vision_item1 = models.CharField(
        max_length=200,
        default='Ilmiy asoslangan yondashuv',
        verbose_name='Qarashlari 1-bandı'
    )

    vision_item2 = models.CharField(
        max_length=200,
        default='Texnologik yangiliklarni joriy etish',
        verbose_name='Qarashlari 2-bandı'
    )

    vision_item3 = models.CharField(
        max_length=200,
        default='Uzluksiz rivojlanish',
        verbose_name='Qarashlari 3-bandı'
    )

    # Button
    button_text = models.CharField(
        max_length=100,
        default='Batafsil ma\'lumot',
        verbose_name='Tugma matni'
    )

    button_link = models.CharField(
        max_length=255,
        default='/about',
        verbose_name='Tugma havolasi'
    )

    button_icon = models.CharField(
        max_length=50,
        default='tji-arrow-right-long',
        verbose_name='Tugma ikona'
    )

    # Background shapes
    bg_shape_1 = models.ImageField(
        upload_to='about/shapes/',
        verbose_name='Fon shakli 1',
        blank=True,
        null=True
    )

    bg_shape_2 = models.ImageField(
        upload_to='about/shapes/',
        verbose_name='Fon shakli 2',
        blank=True,
        null=True
    )

    # Status
    is_active = models.BooleanField(
        default=True,
        verbose_name='Faolmi?'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Yaratilgan vaqti'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='O\'zgartirilgan vaqti'
    )

    class Meta:
        verbose_name = '4. Biz haqimizda'
        verbose_name_plural = '4. Biz haqimizda'
        ordering = ['-created_at']

    def __str__(self):
        return f"Biz haqimizda - {self.sub_title}"

# 4. About progress
class AboutProgress(models.Model):
    """Biz haqimizda progress bar uchun model"""

    about_section = models.ForeignKey(
        AboutSection,
        on_delete=models.CASCADE,
        related_name='progress_items',
        verbose_name='Biz haqimizda bo\'limi'
    )

    title = models.CharField(
        max_length=200,
        verbose_name='Sarlavha'
    )

    percent = models.PositiveIntegerField(
        default=0,
        verbose_name='Foiz miqdori',
        help_text='0 dan 100 gacha'
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Tartib raqami'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Faolmi?'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Yaratilgan vaqti'
    )

    class Meta:
        verbose_name = '4. Progress ko\'rsatkichi'
        verbose_name_plural = '4. Progress ko\'rsatkichlari'
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"{self.title} - {self.percent}%"

# 5. TOP Service Title
class TopServiceSectionHeader(models.Model):
    """Xizmatlar bo'limi sarlavhasi uchun model"""

    sub_title_icon = models.CharField(
        max_length=50,
        default='tji-box',
        verbose_name='Sub-sarlavha ikona',
        help_text='Font Awesome yoki maxsus ikon klassi'
    )

    sub_title = models.CharField(
        max_length=200,
        default='Top Servislar',
        verbose_name='Sub-sarlavha'
    )

    main_title = models.CharField(
        max_length=300,
        default='Biz taqdim etadigan asosiy xizmatlar',
        verbose_name='Asosiy sarlavha'
    )

    button_text = models.CharField(
        max_length=100,
        default='Barcha xizmatlar',
        verbose_name='Tugma matni'
    )

    button_link = models.CharField(
        max_length=255,
        default='/services',
        verbose_name='Tugma havolasi',
        help_text='URL yoki slug'
    )

    button_icon = models.CharField(
        max_length=50,
        default='tji-arrow-right-long',
        verbose_name='Tugma ikona'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Faolmi?',
        help_text='Bo\'lim sarlavhasi faol yoki nofaol'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Yaratilgan vaqti'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='O\'zgartirilgan vaqti'
    )

    class Meta:
        verbose_name = '5. TOP Servis Sarlavhasi'
        verbose_name_plural = '5. TOP Servis Sarlavhasi'
        ordering = ['-created_at']

    def __str__(self):
        return self.main_title

# 5. Top Services
class TopService(models.Model):
    """Xizmatlar uchun model"""

    icon = models.CharField(
        max_length=50,
        verbose_name='Ikona',
        help_text='Font Awesome yoki maxsus ikon klassi (masalan: tji-service-1)'
    )

    title = models.CharField(
        max_length=200,
        verbose_name='Xizmat nomi'
    )

    description = models.TextField(
        verbose_name='Tavsif',
        help_text='Xizmat haqida qisqacha ma\'lumot'
    )

    detail_link = models.CharField(
        max_length=255,
        default='#',
        verbose_name='Batafsil havola',
        help_text='Xizmat tafsiloti sahifasiga havola'
    )

    background_image = models.ImageField(
        upload_to='services/backgrounds/',
        verbose_name='Fon rasmi',
        help_text='Service reveal background uchun rasm'
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Tartib raqami',
        help_text='Kichik raqam birinchi ko\'rsatiladi'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Faolmi?',
        help_text='Xizmat ko\'rsatilsinmi?'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Yaratilgan vaqti'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='O\'zgartirilgan vaqti'
    )

    class Meta:
        verbose_name = '5. TOP Servis'
        verbose_name_plural = '5. TOP Servislar'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

# 6. Texts
class MarqueeItem(models.Model):
    title = models.CharField(
        verbose_name="Sarlavha",
        max_length=100,
        help_text="Marquee bo‘limida chiqadigan matn (masalan: Sifat nazorati, Xavfsizlik va hokazo)."
    )
    image = models.ImageField(
        verbose_name="Rasm",
        upload_to='marquee_images/',
        help_text="Marquee uchun rasm yuklang."
    )
    order = models.PositiveIntegerField(
        verbose_name="Tartib raqami",
        default=0,
        help_text="Marquee elementlarini chiqish tartibini belgilang."
    )
    is_active = models.BooleanField(
        verbose_name="Faolmi?",
        default=True,
        help_text="Agar belgilanmasa, ushbu element sayt sahifasida chiqmaydi."
    )
    created_at = models.DateTimeField(
        verbose_name="Yaratilgan sana",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Yangilangan sana",
        auto_now=True
    )

    class Meta:
        verbose_name = "6. Marquee elementi"
        verbose_name_plural = "6. Marquee elementlari"
        ordering = ['-created_at', 'order']

    def __str__(self):
        return self.title

# 7. Sertificates
class CertificateSectionHeader(models.Model):
    """7. Sertifikatlar bo‘limi sarlavhasi uchun model"""

    sub_title_icon = models.CharField(
        max_length=50,
        default='tji-award',
        verbose_name='Sub-sarlavha ikona',
        help_text='Font Awesome yoki maxsus ikon klassi (masalan: tji-award)'
    )

    sub_title = models.CharField(
        max_length=200,
        default='Bizning sertifikatlarimiz',
        verbose_name='Sub-sarlavha',
        help_text='Masalan: Bizning yutuqlarimiz, Sertifikatlarimiz va hokazo'
    )

    main_title = models.CharField(
        max_length=300,
        default='Sifat va ishonchlilikni tasdiqlovchi sertifikatlarimiz',
        verbose_name='Asosiy sarlavha'
    )

    button_text = models.CharField(
        max_length=100,
        default='Barcha sertifikatlar',
        verbose_name='Tugma matni'
    )

    button_link = models.CharField(
        max_length=255,
        default='/certificates',
        verbose_name='Tugma havolasi',
        help_text='URL yoki slug manzilni kiriting (masalan: /certificates)'
    )

    button_icon = models.CharField(
        max_length=50,
        default='tji-arrow-right-long',
        verbose_name='Tugma ikona',
        help_text='Tugmada chiqadigan ikona (masalan: tji-arrow-right-long)'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Faolmi?',
        help_text='Agar belgilanmasa, ushbu sarlavha sayt sahifasida chiqmaydi.'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Yaratilgan vaqti'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='O‘zgartirilgan vaqti'
    )

    class Meta:
        verbose_name = '7. Sertifikatlar bo‘limi sarlavhasi'
        verbose_name_plural = '7. Sertifikatlar bo‘limi sarlavhasi'
        ordering = ['-created_at']

    def __str__(self):
        return self.main_title

# 7. Sertificate Cards
class CertificateCard(models.Model):
    """7. Sertifikatlar kartasi uchun model"""

    header = models.ForeignKey(
        'CertificateSectionHeader',
        on_delete=models.CASCADE,
        related_name='certificate_cards',
        verbose_name='Bo‘lim sarlavhasi'
    )

    title = models.CharField(
        max_length=255,
        verbose_name='Sertifikat nomi',
        help_text='Masalan: Akkreditatsiya sertifikati'
    )

    description = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Sertifikat tavsifi',
        help_text='Masalan: Sifat kafolatini tasdiqlovchi hujjat'
    )

    image = models.ImageField(
        upload_to='certificates/',
        verbose_name='Sertifikat rasmi',
        help_text='Sertifikatning rasm faylini yuklang'
    )

    link = models.URLField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name='Havola',
        help_text='Agar sertifikat haqida batafsil sahifa bo‘lsa, shu joyga link yozing'
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Tartib raqami',
        help_text='Sertifikatlar chiqarilish tartibini belgilaydi'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Faolmi?',
        help_text='Agar belgilanmasa, ushbu sertifikat sayt sahifasida ko‘rinmaydi'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Yaratilgan vaqti'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='O‘zgartirilgan vaqti'
    )

    class Meta:
        verbose_name = '7. Sertifikat kartasi'
        verbose_name_plural = '7. Sertifikat kartalari'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

# 8. News
class NewsSectionHeader(models.Model):
    """8. Yangiliklar bo‘limi sarlavhasi uchun model"""

    sub_title_icon = models.CharField(
        max_length=50,
        default='tji-news',
        verbose_name='Sub-sarlavha ikona',
        help_text='Font Awesome yoki maxsus ikon klassi (masalan: tji-news)'
    )

    sub_title = models.CharField(
        max_length=200,
        default='So‘nggi yangiliklar',
        verbose_name='Sub-sarlavha',
        help_text='Masalan: Blog, Yangiliklar, O‘quv markazi yangiliklari va hokazo'
    )

    main_title = models.CharField(
        max_length=300,
        default='Bizning markazdagi eng so‘nggi yangiliklardan xabardor bo‘ling',
        verbose_name='Asosiy sarlavha'
    )

    button_text = models.CharField(
        max_length=100,
        default='Barcha yangiliklar',
        verbose_name='Tugma matni'
    )

    button_link = models.CharField(
        max_length=255,
        default='/news',
        verbose_name='Tugma havolasi',
        help_text='URL yoki slug manzilni kiriting (masalan: /news)'
    )

    button_icon = models.CharField(
        max_length=50,
        default='tji-arrow-right-long',
        verbose_name='Tugma ikona',
        help_text='Tugmada chiqadigan ikona (masalan: tji-arrow-right-long)'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Faolmi?',
        help_text='Agar belgilanmasa, ushbu sarlavha sayt sahifasida chiqmaydi.'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Yaratilgan vaqti'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='O‘zgartirilgan vaqti'
    )

    class Meta:
        verbose_name = '8. Yangiliklar bo‘limi sarlavhasi'
        verbose_name_plural = '8. Yangiliklar bo‘limi sarlavhasi'
        ordering = ['-created_at']

    def __str__(self):
        return self.main_title

# Faq
class FaqHeader(models.Model):
    """FAQ bo‘limining asosiy sarlavhasi (chap qism)"""

    image = models.ImageField(
        upload_to='faq/',
        verbose_name="Rasm"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Asosiy sarlavha"
    )
    subtitle = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Qisqa sarlavha"
    )
    call_title = models.CharField(
        max_length=150,
        default="Bepul konsultatsiya",
        verbose_name="Qo‘ng‘iroq sarlavhasi"
    )
    phone_number = models.CharField(
        max_length=30,
        default="+998900000000",
        verbose_name="Telefon raqami"
    )
    phone_icon = models.CharField(
        max_length=50,
        default="tji-phone",
        verbose_name="Telefon ikonka classi"
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
        verbose_name = "9. FAQ sarlavhasi"
        verbose_name_plural = "9. FAQ sarlavhalari"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class FaqItem(models.Model):
    """FAQ bo‘limining savol-javob elementlari (o‘ng qism)"""

    header = models.ForeignKey(
        FaqHeader,
        on_delete=models.CASCADE,
        related_name='faq_items',
        verbose_name="FAQ sarlavhasi"
    )
    question = models.CharField(
        max_length=255,
        verbose_name="Savol"
    )
    answer = models.TextField(
        verbose_name="Javob"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Tartib raqami"
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
        verbose_name = "9. FAQ elementi"
        verbose_name_plural = "9. FAQ elementlari"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.question

