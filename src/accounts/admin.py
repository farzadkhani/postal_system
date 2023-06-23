from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission, User

# Register your models here.


class UserAdmin(BaseUserAdmin):
    list_display = [
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
        "cell_phone",
        "national_code",
    ]

UserAdmin.fieldsets += (
    (
        "Extra Fields",
        {"fields": ("cell_phone", "national_code")},
    ),
)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)