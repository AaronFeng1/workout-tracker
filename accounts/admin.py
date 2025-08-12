from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import UserChangeForm, CustomUserForm

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserForm
    form = UserChangeForm
    list_display = [
        "username",
        "email",
        "age",
        "pk",
    ]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "age",
                    "email",
                    "username",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password1",
                    "password2",
                )
            },
        ),
        ("Personal Info", {"fields": ("email", "age")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
