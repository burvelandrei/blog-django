from django.contrib import admin
from .models import Publication

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'author__username')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'author')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at'),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Publication, PublicationAdmin)