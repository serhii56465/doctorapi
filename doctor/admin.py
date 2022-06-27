from django.contrib import admin

from .models import Area, Doctor


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "slug", "birthday", "experience"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]
    list_filter = ["name", "birthday", "experience", "areas__name"]
