from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User
from social_django.admin import Association, Nonce, UserSocialAuth

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
