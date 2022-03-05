from django.contrib import admin
from . models import Slider, Team, ContactUs

# Register your models here.

admin.site.register(Slider)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'first_name', 'last_name', 'role')
    list_editable = ('role', )

    @admin.display()
    def fullname(self, obj):
        return f'{obj.first_name} {obj.last_name}'.upper()


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'subject', 'company_name')
    list_display_links = ('fullname', 'subject',)
    list_filter = ('company_name', 'subject')