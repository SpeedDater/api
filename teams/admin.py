from django.contrib import admin
from teams.models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    autocomplete_fields = ['member1', 'member2', 'member3', 'member4',
                           'member5', 'availability']
    list_display = ['__str__', 'assigned_section', 'preferred_section']
    list_filter = ['availability', 'preferred_section', 'assigned_section']
    ordering = ['number']
    readonly_fields = ['number']
    search_fields = ['number']
    fieldsets = [
        ('Team Number', {
            'fields': ['number']
        }),
        ('Members', {
            'fields': ['member1', 'member2', 'member3', 'member4', 'member5']
        }),
        ('Availability', {
            'fields': ['availability', 'preferred_section']
        }),
        ('Assignment', {
            'fields': ['assigned_section']
        }),
    ]
