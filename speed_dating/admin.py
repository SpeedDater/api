from django.contrib import admin
from speed_dating.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user', 'availability',
                           'majors', 'interests', 'skills']
    list_display = ['user', 'full_name', 'email']
    list_filter = ['availability', 'majors']
    ordering = ['user']
    readonly_fields = ['email', 'full_name']
    search_fields = ['user__username', 'user__email',
                     'user__first_name', 'user__last_name']
    fieldsets = [
        ('User', {
            'fields': ['user', 'full_name', 'email', 'phone']
        }),
        ('Profile', {
            'fields': ['availability', 'majors', 'skills', 'interests', 'looking_for', 'anything_else'],
        }),
    ]
