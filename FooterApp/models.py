from django.db import models
from tinymce.models import HTMLField


class Information(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان اطلاعات")
    content = HTMLField(verbose_name="توضیحات")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "اطلاعات"
        verbose_name_plural = "اطلاعات"


class Gallery(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان نگاره")
    image = models.ImageField(upload_to="Footer", blank=True, null=True, verbose_name="نگاره")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "نگاره"
        verbose_name_plural = "گالری"




