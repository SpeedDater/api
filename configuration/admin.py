from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView, LogoutView
from configuration.models import *

admin.site.site_header = settings.APP_NAME
admin.site.site_title = settings.APP_NAME
admin.site.index_title = 'Admin Panel'
# use default login views
admin.site.login = LoginView.as_view()
# disable Django groups
admin.site.unregister(Group)


@admin.register(SectionTime)
class SectionTimeAdmin(admin.ModelAdmin):
	search_fields = ['start']
	ordering = ['start', 'end']


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
	change_list_template = 'admin/configuration/change_list_major.html'
	search_fields = ['majors']
	ordering = ['major']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
	change_list_template = 'admin/configuration/change_list_skill.html'
	search_fields = ['skills']
	ordering = ['skill']
