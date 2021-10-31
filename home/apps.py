"""
Application configuration for home app
"""
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Create name attribute that will also act
    as a label for the app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
