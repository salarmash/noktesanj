from django.db import models
from tinymce.models import HTMLField


class Team(models.Model):
    image = models.ImageField(upload_to="Team", blank=True, null=True, verbose_name="نگاره")
    name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    role = models.CharField(max_length=100, verbose_name="پوزیشن شغلی")
    content = HTMLField(verbose_name="توضیحات")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "فرد"
        verbose_name_plural = "تیم"


class Social(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="social")
    image = models.ImageField(upload_to="Team", blank=True, null=True, verbose_name="آیکون")
    title = models.CharField(max_length=100, verbose_name=" نام شبکه اجتماعی")
    role = models.CharField(max_length=100, verbose_name="لینک شبکه اجتماعی")

    class Meta:
        verbose_name = "شبکه اجتماعی"
        verbose_name_plural = "شبکه های اجتماعی"


class Info(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="info")
    label = models.CharField(max_length=255, verbose_name="لیبل")
    value = models.CharField(max_length=255, verbose_name="مقدار")

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "مشخصات فردی"


class Page(models.Model):
    subtitle = models.CharField(max_length=255, verbose_name="عنوان")

    def __str__(self):
        return self.subtitle

    class Meta:
        verbose_name = "تنظیم عنوان"
        verbose_name_plural = "تنظیم عنوان"
