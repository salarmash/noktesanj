from django.db import models
from tinymce.models import HTMLField


class Category(models.Model):
    title = models.CharField(max_length=225, verbose_name="نام دسته بندی")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "نام دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    image = models.ImageField(upload_to="Project", null=True, blank=True, verbose_name="تصویر")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="project", verbose_name="دسته بندی")
    category_slug = models.CharField(max_length=255, verbose_name="اسلاک دسته بندی")
    date = models.CharField(max_length=50, verbose_name="تاریخ اجرای پروژه")
    description = HTMLField(verbose_name="متن")

    def __str__(self):
        return self.title

    def save(
            self,
            *args,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ):
        self.category_slug = self.category.title

        super(Project, self).save()

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه ها"


class Gallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="Project", null=True, blank=True, verbose_name="تصویر")
    alt = models.CharField(max_length=255, verbose_name="عنوان تصویر")

    class Meta:
        verbose_name = "نگاره"
        verbose_name_plural = "گالری"


class Item(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="item")
    label = models.CharField(max_length=255, verbose_name="لیبل")
    value = models.CharField(max_length=255, verbose_name="مقدار")

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتم ها"


class Additional(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name="addtional")
    heading = models.CharField(max_length=255, verbose_name="عنوان")
    content = HTMLField(verbose_name="متن")

    class Meta:
        verbose_name = "توضیحات یشتر"
        verbose_name_plural = "توضیحات بیشتر"


class Page(models.Model):
    subtitle = models.CharField(max_length=255, verbose_name="عنوان")

    def __str__(self):
        return self.subtitle

    class Meta:
        verbose_name = "تنظیم عنوان"
        verbose_name_plural = "تنظیم عنوان"
