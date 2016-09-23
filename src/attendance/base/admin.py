from django.contrib import admin

from . import models


class EntryInline(admin.TabularInline):
    model = models.Entry


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [
        EntryInline,
    ]
