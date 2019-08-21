from django.contrib import admin
from .models import TravelLog


@admin.register(TravelLog)
class TravelLogAdmin(admin.ModelAdmin):
    pass
