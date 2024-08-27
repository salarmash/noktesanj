from django.db import models


class Page(models.Model):
    subtitle = models.CharField(max_length=255, verbose_name="عنوان")

    def __str__(self):
        return self.subtitle

    class Meta:
        verbose_name = "تنظیم عنوان"
        verbose_name_plural = "تنظیم عنوان"


class Form(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام و نام خانوادگی")
    tel = models.CharField(max_length=12, verbose_name="شماره تلفن")
    email = models.EmailField(verbose_name="پست الکترونیکی")
    message = models.TextField(verbose_name="متن پیام")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"


class Info(models.Model):
    phone = models.CharField(max_length=12, verbose_name="شماره تلفن")
    email = models.EmailField(verbose_name="پست الکترونیکی")
    Address = models.TextField(verbose_name="نشانی")

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "اطلاعات تماس"
        verbose_name_plural = "اطلاعات تماس"


class Social(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE, related_name="social")
    title = models.CharField(max_length=255, verbose_name="نام شبکه اجتماعی")
    link = models.CharField(max_length=255, verbose_name="لینک شبکه اجتماعی")
    image = models.ImageField(upload_to="Contact", blank=True, null=True, verbose_name="آیکون شبکه اجتماعی")

    class Meta:
        verbose_name = "شبکه اجتماعی"
        verbose_name_plural = "شبکه های اجتماعی"


class Faq(models.Model):
    subtitle = models.CharField(max_length=255, verbose_name="عنوان")

    def __str__(self):
        return self.subtitle

    class Meta:
        verbose_name = "پرسش و پاسخ"
        verbose_name_plural = "پرسش و پاسخ"


class FaqItem(models.Model):
    faq = models.ForeignKey(Faq, on_delete=models.CASCADE, related_name="item")
    title = models.CharField(max_length=255, verbose_name="سوال")
    text = models.TextField(verbose_name="جواب")

    class Meta:
        verbose_name = "سوالات متدوال"
        verbose_name_plural = "سوالات متدوال"
