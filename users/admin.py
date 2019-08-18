from django.contrib import admin
from .models import Profile, Area
from django.contrib.admin.models import LogEntry

class ProfileAdmin(admin.ModelAdmin):

    def mark_approved(self, request, queryset):
        rows_updated = queryset.update(admin_approved=True)
        if rows_updated == 1:
            message_bit = "1 user was"
        else:
            message_bit = "%s users were" % rows_updated
        self.message_user(request, "%s successfully marked as Approved." % message_bit)
    mark_approved.short_description = "Mark as Approved"

    def mark_unapproved(self, request, queryset):
        rows_updated = queryset.update(admin_approved=False)
        if rows_updated == 1:
            message_bit = "1 user was"
        else:
            message_bit = "%s users were" % rows_updated
        self.message_user(request, "%s successfully marked as Not Approved." % message_bit)
    mark_unapproved.short_description = "Mark as Not Approved"

    list_display = ('user', 'area', 'admin_approved')
    list_filter = ('area',)
    actions = [mark_approved, mark_unapproved]

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
    actions = None

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
