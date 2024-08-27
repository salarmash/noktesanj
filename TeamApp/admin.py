from django.contrib import admin
from .models import Team, Social, Info, Page

admin.site.register(Page)


class SocialAdmin(admin.StackedInline):
    model = Social
    extra = 1


class InfoAdmin(admin.StackedInline):
    model = Info


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = (SocialAdmin, InfoAdmin)
