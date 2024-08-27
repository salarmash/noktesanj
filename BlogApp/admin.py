from django.contrib import admin
from .models import Category, Post, Author, Gallery,Page

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Page)


class GalleryAdmin(admin.StackedInline):
    model = Gallery


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (GalleryAdmin,)
