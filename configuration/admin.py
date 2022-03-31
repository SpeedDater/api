from django.contrib import admin
from configuration import models


@admin.register(models.Section)
class SectionAdmin(admin.ModelAdmin):
	list_display = ['number', 'time']
	search_fields = ['number']
	ordering = ['number']


@admin.register(models.SectionTime)
class SectionTimeAdmin(admin.ModelAdmin):
	search_fields = ['start', 'end']
	ordering = ['start', 'end']


@admin.register(models.Major)
class MajorAdmin(admin.ModelAdmin):
	change_list_template = 'admin/configuration/change_list_major.html'
	search_fields = ['major']
	ordering = ['major']


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
	change_list_template = 'admin/configuration/change_list_skill.html'
	search_fields = ['skill']
	ordering = ['skill']
