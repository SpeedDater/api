from django.contrib import admin
from speed_dating.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	autocomplete_fields = ['user', 'availability', 'interests', 'skills']
	list_display = ['user', 'full_name', 'email']
	ordering = ['user']
	readonly_fields = ['email', 'full_name']
	fieldsets = [
		('User', {
			'fields': ['user', 'full_name', 'email', 'phone']
		}),
		('Profile', {
			'fields': ['availability', 'skills', 'interests', 'looking_for', 'anything_else'],
		}),
	]
