from django.contrib import admin
from .models import Board
from .models import Board, Comments

# Register your models here.
class BaordAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']
    list_display_links = ['id', 'title']

admin.site.register(Board, BaordAdmin)
admin.site.register(Comments)