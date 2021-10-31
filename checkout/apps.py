"""
Application configuration for checkout app
"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Create name attribute that will also act
    as a label for the app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
