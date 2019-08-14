from django.contrib import admin
from .models import Profile, Area

class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'day')
    list_filter = ('name', 'day')

admin.site.register(Profile)
admin.site.register(Area, AreaAdmin)
