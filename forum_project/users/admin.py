from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('display_name', )}),
    )
    # list_display = ['username', 'display_name', 'number_of_posts', 'is_staff']


admin.site.register(CustomUser, CustomUserAdmin)
