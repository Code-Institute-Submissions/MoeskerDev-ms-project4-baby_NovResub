"""
Application configuration for basket app
"""
from django.apps import AppConfig


class BasketConfig(AppConfig):
    """
    Create name attribute that will also act
    as a label for the app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basket'
