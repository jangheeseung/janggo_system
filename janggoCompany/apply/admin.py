from django.contrib import admin
from .models import Hire, Apply

# Register your models here.
class HireAdmin(admin.ModelAdmin):
    list_display = ['id', 'kind', 'start_date', 'end_date']
    list_display_links = ['id', 'kind']
class ApplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'hire']
    list_display_links = ['id', 'name']

admin.site.register(Hire, HireAdmin)
admin.site.register(Apply, ApplyAdmin)