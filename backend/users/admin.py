from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'role', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'role',)}),
    )

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'headline']

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
