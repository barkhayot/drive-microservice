from django.db import models

# Create your models here.
class Drive(models.Model):
    driver              = models.IntegerField()
    leaving_city        = models.CharField(max_length=255, verbose_name="Leaving City")
    going_city          = models.CharField(max_length=255, verbose_name="Going City")
    date                = models.DateField()
    leaving_time        = models.TimeField()
    coming_time         = models.TimeField()
    passengers          = models.IntegerField()
    price               = models.CharField(max_length=50, default="Free")
    car                 = models.CharField(max_length=255, verbose_name="Model of Car")
    created_at          = models.DateTimeField(auto_now_add=True)
    contact             = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.leaving_city} to {self.going_city}'