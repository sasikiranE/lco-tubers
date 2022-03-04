from django.contrib import admin
from . models import Slider, Team

# Register your models here.

admin.site.register(Slider)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'first_name', 'last_name', 'role')
    list_editable = ('role', )

    @admin.display()
    def fullname(self, obj):
        return f'{obj.first_name} {obj.last_name}'.upper()
