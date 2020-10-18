from django.contrib import admin

from .models import Clockin


# admin.site.register(Clockin)

@admin.register(Clockin)
class ClockinAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
