from django.contrib import admin

from .models import Recording

class RecordingAdmin(admin.ModelAdmin):

    list_display = ('recorded_at', 'recorded_by', 'url', 'duration')

admin.site.register(Recording, RecordingAdmin)
