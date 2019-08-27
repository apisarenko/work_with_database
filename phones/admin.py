from django.contrib import admin
from .models import Phone


@admin.register(Phone)
class PersonAdmin(admin.ModelAdmin):
    pass
