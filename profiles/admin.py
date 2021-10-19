"""
To register and display the models in the Django admin
"""
from django.contrib import admin
from .models import UserProfile, WishList


class UserProfileAdmin(admin.ModelAdmin):
    """
    Adding certain UserProfile fields in Django admin
    """
    list_display = (
        'user',
        'default_postcode',
        'default_town_or_city',
        'default_county',
        'default_country',
    )


class WishListAdmin(admin.ModelAdmin):
    """
    Adding certain WishList fields in Django admin
    """
    list_display = (
        'user',
    )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(WishList, WishListAdmin)
