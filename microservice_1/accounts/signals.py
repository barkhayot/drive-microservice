from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import UserProfile, Account
from django.conf import settings

# @receiver(post_save, sender=Profile)


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = UserProfile.objects.create(
            user=user,
            
        )


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.save()


def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


post_save.connect(createProfile, sender=Account)
post_save.connect(updateUser, sender=UserProfile)
post_delete.connect(deleteUser, sender=UserProfile)