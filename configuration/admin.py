from django.contrib import admin
from configuration.models import *


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
