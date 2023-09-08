from django.contrib import admin

from clubs.models import *


class CamerasAdmin(admin.ModelAdmin):
    list_display = ('ip', 'location', 'club')
    search_fields = ('ip', 'location', 'club')


admin.site.register(Club)
admin.site.register(Camera, CamerasAdmin)
admin.register(Picture)
