from django.contrib import admin
from configuration.models import *


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
	list_display = ['number', 'time']
	search_fields = ['number']
	ordering = ['number']


@admin.register(SectionTime)
class SectionTimeAdmin(admin.ModelAdmin):
	search_fields = ['start', 'end']
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
