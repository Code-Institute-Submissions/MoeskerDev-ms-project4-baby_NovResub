"""
To create a separate storage of static and media files
"""
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    To set a location for static files
    """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """
    To set a location for media files
    """
    location = settings.MEDIAFILES_LOCATION
