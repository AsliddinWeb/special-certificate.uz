from django.db import models

# About Page
class AboutPageTitle(models.Model):
    title_about = models.CharField(
        max_length=200,
        verbose_name="About sahifasi sarlavhasi"
    )
    title_home = models.CharField(
        max_length=200,
        verbose_name="Bosh sahifa sarlavhasi"
    )
    client_text = models.TextField(verbose_name="Client logo text", null=True, blank=True)

    class Meta:
        verbose_name = "1. About Sahifa sarlavhasi"
        verbose_name_plural = "1. About Sahifa sarlavhalari"

    def __str__(self):
        return f"Sahifa sarlavhalari"


class TeamSection(models.Model):
    """Team section uchun sarlavha va sub-title"""
    sub_title = models.CharField(
        max_length=100,
        default="Meet Our Team",
        verbose_name="Sub Title"
    )
    main_title = models.CharField(
        max_length=200,
        default="Success Stories Fuel our Innovation.",
        verbose_name="Main Title"
    )
    is_active = models.BooleanField(default=True, verbose_name="Active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "2. Jamoa bo'limi sarlavhasi"
        verbose_name_plural = "2. Jamoa bo'limi sarlavhasi"
        ordering = ['-created_at']

    def __str__(self):
        return self.main_title


class TeamMember(models.Model):
    """Jamoa a'zolari uchun model"""
    full_name = models.CharField(max_length=100, verbose_name="To'liq ismi")
    designation = models.CharField(max_length=100, verbose_name="Lavozimi")
    image = models.ImageField(
        upload_to='team/',
        verbose_name="Rasm"
    )
    email = models.EmailField(verbose_name="Email", blank=True)

    # Social media links
    facebook_url = models.URLField(blank=True, verbose_name="Facebook")
    instagram_url = models.URLField(blank=True, verbose_name="Instagram")
    twitter_url = models.URLField(blank=True, verbose_name="Twitter/X")
    linkedin_url = models.URLField(blank=True, verbose_name="LinkedIn")

    # Ordering va status
    order = models.IntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "3. Jamoa A'zosi"
        verbose_name_plural = "3. Jamoa A'zolari"
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.designation}"


# Contact page
class ContactHeader(models.Model):
    title = models.CharField(
        max_length=200,
        default="Contact Us",
        verbose_name="Sarlavha"
    )
    background_image = models.ImageField(
        upload_to='contact/backgrounds/',
        verbose_name="Fon rasmi"
    )
    overlay_image = models.ImageField(
        upload_to='contact/overlays/',
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
        verbose_name = "4. Aloqa sahifasi sarlavhasi"
        verbose_name_plural = "4. Aloqa sahifasi sarlavhalari"

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    # Section heading
    subtitle = models.CharField(
        max_length=100,
        default="Aloqa ma'lumotlari",
        verbose_name="Kichik sarlavha"
    )
    title = models.CharField(
        max_length=200,
        default="Biz bilan bog'laning",
        verbose_name="Asosiy sarlavha"
    )
    title_highlight = models.CharField(
        max_length=100,
        default="Biz",
        verbose_name="Ajratilgan so'z",
        help_text="Sarlavhadagi rang bilan ajratilgan so'z"
    )

    class Meta:
        verbose_name = "4. Aloqa ma'lumotlari bo'limi"
        verbose_name_plural = "4. Aloqa ma'lumotlari bo'limlari"

    def __str__(self):
        return self.title


class ContactItem(models.Model):
    ICON_CHOICES = [
        ('tji-location-3', 'Manzil'),
        ('tji-envelop', 'Email'),
        ('tji-phone', 'Telefon'),
        ('tji-chat', 'Chat'),
    ]

    contact_info = models.ForeignKey(
        ContactInfo,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="Aloqa ma'lumotlari"
    )
    icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        verbose_name="Ikonka"
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Sarlavha"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Tavsif",
        help_text="Manzil uchun ishlatiladi"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Tartib"
    )
    animation_delay = models.CharField(
        max_length=10,
        default=".3s",
        verbose_name="Animatsiya kechikishi"
    )

    class Meta:
        verbose_name = "4. Aloqa elementi"
        verbose_name_plural = "4. Aloqa elementlari"
        ordering = ['order']

    def __str__(self):
        return self.title


class ContactItemDetail(models.Model):
    contact_item = models.ForeignKey(
        ContactItem,
        on_delete=models.CASCADE,
        related_name='details',
        verbose_name="Aloqa elementi"
    )
    link_type = models.CharField(
        max_length=20,
        choices=[
            ('email', 'Email'),
            ('tel', 'Telefon'),
            ('url', 'Havola'),
        ],
        verbose_name="Havola turi"
    )
    link_value = models.CharField(
        max_length=200,
        verbose_name="Havola qiymati",
        help_text="Email, telefon raqami yoki URL"
    )
    display_text = models.CharField(
        max_length=200,
        verbose_name="Ko'rsatiladigan matn"
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name="Faol",
        help_text="Active klassini qo'shish uchun"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Tartib"
    )

    class Meta:
        verbose_name = "4. Aloqa elementi tafsiloti"
        verbose_name_plural = "4. Aloqa elementi tafsilotlari"
        ordering = ['order']

    def __str__(self):
        return self.display_text

    def get_link_url(self):
        """Havola turini qaytaradi"""
        if self.link_type == 'email':
            return f"mailto:{self.link_value}"
        elif self.link_type == 'tel':
            return f"tel:{self.link_value}"
        return self.link_value


class ContactForm(models.Model):
    full_name = models.CharField(
        max_length=200,
        verbose_name="To'liq ism"
    )
    email = models.EmailField(
        verbose_name="Email"
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Telefon raqami"
    )
    subject = models.CharField(
        max_length=200,
        verbose_name="Mavzu",
        blank=True,
        null=True
    )
    message = models.TextField(
        verbose_name="Xabar"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Yuborilgan vaqti"
    )
    is_read = models.BooleanField(
        default=False,
        verbose_name="O'qilgan"
    )

    class Meta:
        verbose_name = "4. Aloqa formasi"
        verbose_name_plural = "4. Aloqa formalari"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.created_at.strftime('%d.%m.%Y')}"


class ContactFormSettings(models.Model):
    title = models.CharField(
        max_length=300,
        default="Feel Free to Get in Touch or Visit our Location",
        verbose_name="Sarlavha"
    )

    # Form field labels
    full_name_label = models.CharField(
        max_length=100,
        default="Full Name",
        verbose_name="Ism maydon nomi"
    )
    email_label = models.CharField(
        max_length=100,
        default="Email Address",
        verbose_name="Email maydon nomi"
    )
    phone_label = models.CharField(
        max_length=100,
        default="Phone Number",
        verbose_name="Telefon maydon nomi"
    )
    message_label = models.CharField(
        max_length=100,
        default="Type message",
        verbose_name="Xabar maydon nomi"
    )
    submit_button_text = models.CharField(
        max_length=100,
        default="Submit Now",
        verbose_name="Yuborish tugmasi matni"
    )

    # Success/Error messages
    success_message = models.CharField(
        max_length=200,
        default="Your message has been sent successfully!",
        verbose_name="Muvaffaqiyatli xabar"
    )
    error_message = models.CharField(
        max_length=200,
        default="Please fill in all required fields!",
        verbose_name="Xato xabari"
    )

    map_url = models.URLField(
        verbose_name="Xarita URL",
        help_text="Google Maps embed URL"
    )
    animation_delay = models.CharField(
        max_length=10,
        default=".1s",
        verbose_name="Forma animatsiya kechikishi"
    )
    map_animation_delay = models.CharField(
        max_length=10,
        default=".3s",
        verbose_name="Xarita animatsiya kechikishi"
    )

    class Meta:
        verbose_name = "4. Aloqa formasi sozlamalari"
        verbose_name_plural = "4. Aloqa formasi sozlamalari"

    def __str__(self):
        return self.title

class CtaSection(models.Model):
    title = models.CharField(
        max_length=300,
        default="Let's Build Future Together.",
        verbose_name="Sarlavha"
    )
    button_text = models.CharField(
        max_length=100,
        default="Get Started Now",
        verbose_name="Tugma matni"
    )
    button_link = models.CharField(
        max_length=200,
        default="contact.html",
        verbose_name="Tugma havolasi"
    )
    background_image = models.ImageField(
        upload_to='cta/',
        verbose_name="Fon rasmi"
    )
    animation_delay = models.CharField(
        max_length=10,
        default=".6s",
        verbose_name="Animatsiya kechikishi"
    )

    class Meta:
        verbose_name = "4. CTA bo'limi"
        verbose_name_plural = "4. CTA bo'limlari"

    def __str__(self):
        return self.title