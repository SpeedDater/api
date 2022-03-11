from django.contrib import admin
from speed_dating.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user', 'current_section', 'availability',
                           'majors', 'interests', 'skills']
    list_display = ['user', 'full_name', 'email', 'current_section']
    list_filter = ['current_section', 'availability']
    ordering = ['user']
    readonly_fields = ['email', 'full_name']
    search_fields = ['user__username', 'user__email',
                     'user__first_name', 'user__last_name']
    fieldsets = [
        ('User', {
            'fields': ['user', 'full_name', 'email', 'phone']
        }),
        ('Section', {
            'fields': ['current_section', 'availability']
        }),
        ('Profile', {
            'fields': ['majors', 'skills', 'interests', 'looking_for', 'anything_else']
        }),
    ]
