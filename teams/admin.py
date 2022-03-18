from django.contrib import admin
from teams.models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    autocomplete_fields = ['members', 'availability']
    list_display = ['__str__', 'assigned_section', 'preferred_section']
    list_filter = ['availability', 'preferred_section', 'assigned_section']
    ordering = ['number']
    readonly_fields = ['number']
    search_fields = ['number', 'members__username', 'members__email',
                     'members__first_name', 'members__last_name']
    fieldsets = [
        ('Team Number', {
            'fields': ['number']
        }),
        ('Members', {
            'fields': ['members']
        }),
        ('Availability', {
            'fields': ['availability', 'preferred_section'],
        }),
        ('Assignment', {
            'fields': ['assigned_section'],
        }),
    ]
