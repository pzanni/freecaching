# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return 'Profile for ' + self.user.username


class Geocache(models.Model):
    name = models.CharField(max_length=200)
    lat = models.FloatField()
    lon = models.FloatField()
    description = models.CharField(max_length=1000)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

