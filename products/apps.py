"""
Application configuration of the app
"""
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """
    Create name attribute that will also act
    as a label for the app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
