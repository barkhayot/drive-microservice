from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class AccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, username, password=None):
        if not email:
            raise ValueError("User must have an email")

        if not username:
            raise ValueError("User must have a username")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser =True

        user.save(using=self._db)
        
        return user


class Account(AbstractBaseUser):
    first_name      = models.CharField(max_length=50, verbose_name="First Name")
    last_name       = models.CharField(max_length=50, verbose_name="Last Name")
    username        = models.CharField(max_length=50, unique=True, verbose_name="Username")
    email           = models.EmailField(max_length=100, unique=True, verbose_name="Email Address")

    # required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']


    objects = AccountManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

# Models for Drive Features

class Featured_Music(models.Model):
    music       = models.CharField(max_length=255, verbose_name="Comment for Music")
    
    def __str__(self):
        return self.music

class Featured_Talking(models.Model):
    talking     = models.CharField(max_length=255, verbose_name="Comment for Talking")

    def __str__(self):
        return self.talking

class Featured_Smoking(models.Model):
    smoking     = models.CharField(max_length=255, verbose_name="Comment for Smoking")

    def __str__(self):
        return self.smoking

class Featured_Pets(models.Model):
    pets        = models.CharField(max_length=255, verbose_name="Comment for Pets")

    def __str__(self):
        return self.pets


# User Profile Model

class UserProfile(models.Model):
    user            = models.OneToOneField(Account, unique=True, primary_key=True, on_delete=models.CASCADE)
    age             = models.IntegerField(blank=True, null=True, verbose_name="Age")
    about           = models.TextField(max_length=1000, blank=True, null=True, verbose_name='About')
    experience      = models.IntegerField(blank=True, null=True, verbose_name="Experience of driving")
    over_drive      = models.IntegerField(blank=True, null=True, verbose_name="Over Drive")
    address_line    = models.CharField(blank=True, null=True,max_length=100, verbose_name="Address Line")
    city            = models.CharField(blank=True, null=True, max_length=20, verbose_name="City")
    state           = models.CharField(blank=True, null=True, max_length=20, verbose_name="State")
    country         = models.CharField(blank=True, null=True, max_length=20, verbose_name="Country")

    # More About Drive (Featured)
    music           = models.ForeignKey(Featured_Music, on_delete=models.SET_NULL, related_name='userprofile', blank=True, null=True)
    talking         = models.ForeignKey(Featured_Talking, on_delete=models.SET_NULL, related_name='userprofile', blank=True, null=True)
    smoking         = models.ForeignKey(Featured_Smoking, on_delete=models.SET_NULL, related_name='userprofile', blank=True, null=True)
    pets            = models.ForeignKey(Featured_Pets, on_delete=models.SET_NULL, related_name='userprofile', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=Account)
    def create_user_profile( sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=Account)
    def save_user_profile( sender, instance, **kwargs):
        instance.userprofile.save()