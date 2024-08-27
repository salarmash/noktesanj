from django.db import models


class Page(models.Model):
    subtitle = models.CharField(max_length=255, verbose_name="عنوان")

    def __str__(self):
        return self.subtitle

    class Meta:
        verbose_name = "تنظیم عنوان"
        verbose_name_plural = "تنظیم عنوان"


class About(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان")
    description = models.TextField(verbose_name="متن")
    image = models.ImageField(upload_to="About", blank=True, null=True, verbose_name="نگاره")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"


class Counter(models.Model):
    about = models.ForeignKey(About, models.CASCADE, related_name="counter")
    label = models.CharField(max_length=255, verbose_name="عنوان")
    value = models.PositiveSmallIntegerField(default=0, verbose_name="مقدار")

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "شمارنده"
        verbose_name_plural = "شمارنده ها"


class Gallery(models.Model):
    image1 = models.ImageField(upload_to="About", blank=True, null=True, verbose_name="نگاره 1")
    image2 = models.ImageField(upload_to="About", blank=True, null=True, verbose_name="نگاره 2")

    class Meta:
        verbose_name = "عکس"
        verbose_name_plural = "گالری"


class Award(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "جایزه"
        verbose_name_plural = "جوائز"


class AwardItem(models.Model):
    award = models.ForeignKey(Award, on_delete=models.CASCADE, related_name='awardItem')
    image = models.ImageField(upload_to="About", blank=True, null=True, verbose_name="نگاره")
    title = models.CharField(max_length=255, verbose_name="لیبل")

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتم ها"


class History(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "تاریخچه"
        verbose_name_plural = "تاریخچه"


class HistoryItem(models.Model):
    history = models.ForeignKey(History, on_delete=models.CASCADE, related_name='historyItems')
    title = models.CharField(max_length=255, verbose_name="عنوان")
    year = models.CharField(max_length=5, verbose_name="سال")
    image = models.ImageField(upload_to="About", blank=True, null=True, verbose_name="نگاره")
    text = models.TextField(verbose_name="متن ")

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتم ها"


class Partner(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "همکاران"
        verbose_name_plural = "همکاران"


class PartnerItem(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='partnerItems')
    title = models.CharField(max_length=255, verbose_name="عنوان")
    link = models.CharField(max_length=255, verbose_name="لینک")
    image = models.ImageField(upload_to="About", blank=True, null=True, verbose_name="نگاره")

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتم ها"
