from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Page(models.Model):
    subtitle = models.CharField(max_length=255, verbose_name="عنوان")

    def __str__(self):
        return self.subtitle

    class Meta:
        verbose_name = "تنظیم عنوان"
        verbose_name_plural = "تنظیم عنوان"


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="دسته بندی")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title


class Author(models.Model):
    fullname = models.CharField(max_length=255, verbose_name="نام نویسنده")
    user = models.OneToOneField(User, related_name="authors", verbose_name=" یوزر", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسندگان"

    def __str__(self):
        return self.fullname


class Post(models.Model):
    image = models.ImageField(upload_to="Blog", blank=True, null=True, verbose_name="تصویر مطلب")
    title = models.CharField(max_length=255, verbose_name="عنوان بلاگ")
    short = models.CharField(max_length=255, verbose_name="کوتاه نوشت", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey(Category, related_name="posts", verbose_name="دسته بندی", on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name="posts", on_delete=models.CASCADE, verbose_name="نویسنده")
    content1 = HTMLField(verbose_name="متن بخش اول")
    content2 = HTMLField(verbose_name="متن بخش دوم", null=True, blank=True)

    class Meta:
        verbose_name = "مطلب"
        verbose_name_plural = "بلاگ ها"
        ordering = ('-date',)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to="Blog", blank=True, null=True, verbose_name="تصویر ")

    class Meta:
        verbose_name = "نگاره"
        verbose_name_plural = "گالری"
