from django.contrib import admin
from .models import Profile, Area
from django.contrib.admin.models import LogEntry

class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'day')
    list_filter = ('name', 'day')

class LogEntryAdmin(admin.ModelAdmin):
    readonly_fields = ('content_type',
        'user',
        'action_time',
        'object_id',
        'object_repr',
        'action_flag',
        'change_message'
    )
    list_display = ('user', 'action_flag', 'object_repr')

admin.site.register(Profile)
admin.site.register(Area, AreaAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
