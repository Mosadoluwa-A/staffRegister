from django.contrib import admin

from .models import Clockin
from .models import Absent


# admin.site.register(Absent)


@admin.register(Clockin, Absent)
class ClockinAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

