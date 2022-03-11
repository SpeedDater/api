from django.contrib import admin
from teams.models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    autocomplete_fields = ['members', 'availability']
    list_filter = ['availability', 'preferred_section']
    ordering = ['id']
    readonly_fields = ['id']
    search_fields = ['id', 'members__username', 'members__email',
                     'members__first_name', 'members__last_name']
    fieldsets = [
        ('Team Number', {
            'fields': ['id']
        }),
        ('Members', {
            'fields': ['members']
        }),
        ('Availability', {
            'fields': ['availability', 'preferred_section'],
        }),
    ]
