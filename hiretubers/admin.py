from django.contrib import admin
from . models import Hiretuber

# Register your models here.
@admin.register(Hiretuber)
class HiretuberAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'city', 'phone', 'message')
    list_display_links = ('fullname', 'city')
    list_filter = ('city', 'message')

    @admin.display()
    def fullname(self, obj):
        return f'{obj.first_name} {obj.last_name}'