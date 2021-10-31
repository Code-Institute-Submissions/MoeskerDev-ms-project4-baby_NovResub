"""
Application configuration of the app
"""
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Create name attribute that will also act
    as a label for the app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
