from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User

# set admin site name
admin.site.site_header = settings.APP_NAME
admin.site.site_title = settings.APP_NAME
admin.site.index_title = 'Admin Panel'
# disable Django groups
admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(User)
class UserAdminWithActions(UserAdmin):
	actions = ['disable_password_login', 'grant_staff_privileges', 'remove_staff_privileges']

	def disable_password_login(modeladmin, request, queryset):
		for u in queryset:
			u.set_unusable_password()
			u.save()

	def grant_staff_privileges(modeladmin, request, queryset):
		for u in queryset:
			u.is_staff = True
			u.is_superuser = True
			u.save()
	
	def remove_staff_privileges(modeladmin, request, queryset):
		for u in queryset:
			u.is_staff = False
			u.is_superuser = False
			u.save()
