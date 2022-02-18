from django.contrib import admin
from django.contrib.auth.models import Group
from configuration.models import *

admin.site.site_header = 'SpeedDater407'
admin.site.site_title = 'SpeedDater407'
admin.site.index_title = 'Admin Panel'

admin.site.unregister(Group)
admin.site.register(Major)
admin.site.register(SectionTime)
admin.site.register(Skill)
