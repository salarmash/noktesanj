from django.contrib import admin
from .models import Form, Info, Social, Faq, FaqItem,Page

admin.site.register(Form)
admin.site.register(Page)


class SocialAdmin(admin.StackedInline):
    model = Social
    extra = 1


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    inlines = (SocialAdmin,)


class FaqItemAdmin(admin.StackedInline):
    model = FaqItem
    extra = 2


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    inlines = (FaqItemAdmin,)
