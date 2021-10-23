"""
To register and display the models in the Django admin
"""
from django.contrib import admin
from .models import Review, UserProfile, WishList


class ReviewAdmin(admin.ModelAdmin):
    """
    Adding Review fields in Django admin
    """
    list_display = (
        'user',
        'product',
        'rating',
        'review',
    )


class UserProfileAdmin(admin.ModelAdmin):
    """
    Adding UserProfile fields in Django admin
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
    Adding WishList fields in Django admin
    """
    list_display = (
        'user',
        'product',
    )


admin.site.register(Review, ReviewAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(WishList, WishListAdmin)
