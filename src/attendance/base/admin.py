from django.contrib import admin

from . import models


class EntryInline(admin.TabularInline):
    model = models.Entry


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ['matriculation']
    inlines = [
        EntryInline,
    ]

@admin.register(models.Entry)
class EntryAdmin(admin.ModelAdmin):
    search_fields = ['student__matriculation']
    list_filter = ['direction', 'auto']
