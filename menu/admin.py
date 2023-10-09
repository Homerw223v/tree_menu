from django.contrib import admin

from .models import Menu


@admin.register(Menu)
class TreeMenuAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'parent']
    list_display = ['__str__', 'url', 'parent']
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        ordering = ['parent']
