from django.contrib import admin
from . models import Youtuber

# Register your models here.

@admin.register(Youtuber)
class YoutuberAdmin(admin.ModelAdmin):
    list_display = ('name', 'subs_count', 'camera_type', 'crew', 'is_featured')
    list_editable = ('subs_count', 'camera_type', 'crew', 'is_featured')
    list_filter = ('camera_type', 'subs_count', 'crew', 'is_featured')
    search_fields = ('name', 'camera_type')
