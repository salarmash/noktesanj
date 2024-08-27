from django.contrib import admin
from .models import About, Counter, Gallery, Award, AwardItem, History, HistoryItem, Partner, PartnerItem, Page

admin.site.register(Page)
admin.site.register(Gallery)


class CounterAdmin(admin.StackedInline):
    model = Counter


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = (CounterAdmin,)


class AwardItemAdmin(admin.StackedInline):
    model = AwardItem


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    inlines = (AwardItemAdmin,)


class HistoryItemAdmin(admin.StackedInline):
    model = HistoryItem


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    inlines = (HistoryItemAdmin,)


class PartnerItemAdmin(admin.StackedInline):
    model = PartnerItem


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    inlines = (PartnerItemAdmin,)
