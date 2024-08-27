from django.db import models
from tinymce.models import HTMLField


class Hero(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان")
    image = models.ImageField(upload_to="Service", blank=True, null=True, verbose_name="آیکون")
    video = models.FileField(upload_to="Service", blank=True, null=True, verbose_name="ویدئو")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "هدر"
        verbose_name_plural = "هدر"


class About(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان سکشن")
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان سکشن")
    title1 = models.CharField(max_length=100, verbose_name="عنوان متن اول")
    text1 = HTMLField(verbose_name="توضیح متن اول")
    title2 = models.CharField(max_length=100, verbose_name="عنوان متن دوم")
    text2 = HTMLField(verbose_name="توضیح متن دوم")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"
