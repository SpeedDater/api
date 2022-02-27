from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User
from social_django.admin import Association, Nonce, UserSocialAuth
from configuration.models import *

# set admin site name
admin.site.site_header = settings.APP_NAME
admin.site.site_title = settings.APP_NAME
admin.site.index_title = 'Admin Panel'
# disable Django groups
admin.site.unregister(Group)
admin.site.unregister(User)
# disable python-social-auth modules
admin.site.unregister(Association)
admin.site.unregister(Nonce)
admin.site.unregister(UserSocialAuth)


@admin.register(User)
class UserAdminWithActions(UserAdmin):
	actions = ['remove_password']

	def remove_password(modeladmin, request, queryset):
		for u in queryset:
			u.set_unusable_password()
			u.save()
	remove_password.short_description = "Remove password"


@admin.register(SectionTime)
class SectionTimeAdmin(admin.ModelAdmin):
	search_fields = ['start']
	ordering = ['start', 'end']


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
	change_list_template = 'admin/configuration/change_list_major.html'
	search_fields = ['major']
	ordering = ['major']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
	change_list_template = 'admin/configuration/change_list_skill.html'
	search_fields = ['skill']
	ordering = ['skill']
