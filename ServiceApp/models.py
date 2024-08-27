from django.db import models
from tinymce.models import HTMLField


class Page(models.Model):
    subtitle = models.CharField(max_length=255, verbose_name="عنوان")

    def __str__(self):
        return self.subtitle

    class Meta:
        verbose_name = "تنظیم عنوان"
        verbose_name_plural = "تنظیم عنوان"


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان")
    text = HTMLField(verbose_name="توضیحات")
    video = models.FileField(upload_to="Service", blank=True, null=True, verbose_name="ویدئو")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "توضیح سرویس"
        verbose_name_plural = "توضیح سرویس"


class Items(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    image = models.ImageField(upload_to="Service", blank=True, null=True, verbose_name="نگاره")
    content = HTMLField(verbose_name="توضیحات")
    title2 = models.CharField(max_length=100, verbose_name="عنوان دوم")
    content2 = HTMLField(verbose_name="توضیحات دوم")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتم ها"




class FAQ(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='faq')
    title_faq = models.CharField(max_length=255, verbose_name="عنوان ")

    class Meta:
        verbose_name = "سوال متداول"
        verbose_name_plural = "سوالات متداول"

    def __str__(self):
        return self.title_faq


class FAQItem(models.Model):
    faq = models.ForeignKey(FAQ, related_name='faqItems', on_delete=models.CASCADE)
    label = models.CharField(max_length=255, verbose_name="سوال")
    text = HTMLField(verbose_name="جواب")

    class Meta:
        verbose_name = "پرسش و پاسخ"
        verbose_name_plural = "پرسشها و پاسخ ها"
