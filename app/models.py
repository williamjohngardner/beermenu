from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Restaurant(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Beer(models.Model):
    beer_name = models.CharField(max_length=50)
    brewer_name = models.CharField(max_length=50)
    beer_type = models.CharField(max_length=30)
    abv = models.DecimalField(max_digits=5, decimal_places=2)
    restaurant = models.ManyToManyField(Restaurant)

    def __str__(self):
        return self.beer_name

class UserProfile(models.Model):
    user = models.ForeignKey("auth.User")
    user_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.user_name


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get("created")
    instance = kwargs.get("instance")

    if created:
        UserProfile.objects.create(user=instance)
