from django.contrib import admin
from .models import Page, Service, Items, FAQ, FAQItem

admin.site.register(Page)
admin.site.register(Service)
admin.site.register(Items)




class FAQItemAdmin(admin.StackedInline):
    model = FAQItem


@admin.register(FAQ)
class FaqAdmin(admin.ModelAdmin):
    inlines = (FAQItemAdmin,)
