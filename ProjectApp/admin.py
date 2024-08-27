from django.contrib import admin
from .models import Category, Project, Gallery, Item, Additional, Page

admin.site.register(Category)
admin.site.register(Page)


class GalleryAdmin(admin.StackedInline):
    model = Gallery


class ItemAdmin(admin.StackedInline):
    model = Item
    extra = 1


class AddAdmin(admin.StackedInline):
    model = Additional


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = (GalleryAdmin, ItemAdmin, AddAdmin)
    exclude = ("category_slug",)
