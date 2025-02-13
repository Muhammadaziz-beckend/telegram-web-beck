from django.contrib import admin

from .models import UserI


@admin.register(UserI)
class UserIAdmin(admin.ModelAdmin):
    list_display = ("id",)

    list_display_links = ("id",)
