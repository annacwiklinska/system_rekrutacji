from django.contrib import admin

# Register your models here.
from .models import Uczelnia, KierunekStudiow


@admin.register(Uczelnia)
class UczelniaAdmin(admin.ModelAdmin):
    list_display = ['nazwa']
    # pass
    # list_display = [field.name for field in Uczelnia._meta.get_fields() if field.name != "id"]


@admin.register(KierunekStudiow)
class KierunekStudiowAdmin(admin.ModelAdmin):
    # list_display = ['']
    # pass
    list_display = [field.name for field in KierunekStudiow._meta.get_fields() if field.name != "id" and field.name != "opis"]
