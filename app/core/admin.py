from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["email", "first_name", "last_name", "is_activate"]
    list_filter = []
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal Info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "deleted",
                    "type_user",
                )
            },
        ),
        (_("Permissions"), {"fields": ("is_activate", "is_staff", "is_superuser")}),
        (_("Important dates"), {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.PersonalProfile)
admin.site.register(models.ProfileCompany)
admin.site.register(models.ProfileAssociation)
admin.site.register(models.Category)
admin.site.register(models.CampaingHeader)
admin.site.register(models.CampaingBody)
admin.site.register(models.Currency)
admin.site.register(models.Accumulated)
admin.site.register(models.Payment)
admin.site.register(models.Comment)
admin.site.register(models.Reward)
admin.site.register(models.Favorite)
admin.site.register(models.Like)
admin.site.register(models.Country)
admin.site.register(models.City)
admin.site.register(models.SocialNetworkPP)
admin.site.register(models.SocialNetworkPA)
admin.site.register(models.SocialNetworkPC)
admin.site.register(models.Phase)
admin.site.register(models.Improve)
admin.site.register(models.BookMark)
admin.site.register(models.Upload)
