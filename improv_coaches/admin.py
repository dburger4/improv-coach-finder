from django.contrib import admin
from .models import ImprovCoach

# Register your models here.

class ImprovCoachAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date")

admin.site.register(ImprovCoach, ImprovCoachAdmin)
