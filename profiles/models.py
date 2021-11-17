"""
Modules for the profiles app
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField
from products.models import Product


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_county = models.CharField(
        max_length=80, null=True, blank=True)
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        # pylint: disable=maybe-no-member
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # pylint: disable=unused-argument
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


class WishList(models.Model):
    """
    A wishlist model to maintain a list of
    products a logged in user wishes to buy
    """
    user = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return str(self.user)


# RATING_CHOICES = [
#     (1, 1),
#     (2, 2),
#     (3, 3),
#     (4, 4),
#     (5, 5),
# ]


class Review(models.Model):
    """
    A review model to maintain reviews and ratings
    about the products made by a registered user
    """
    user = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.CASCADE)
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, null=False)
    # choices=RATING_CHOICES
    review = models.TextField(null=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.user)
