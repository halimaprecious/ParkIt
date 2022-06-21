
from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Location(models.Model):
    place = models.CharField(max_length=244)

    def __str__(self):
        return self.place

    def save_location(self):
        return self.save()
    
class BookedSlot(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,)
    # slot_id = models.ForeignKey(ParkSlot, on_delete=models.CASCADE,)


class ParkSlot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    slot_name = models.CharField(max_length=50)
    image =models.ImageField(upload_to='parkslots/')
    booked =models.BooleanField(default =False)
    booked_slot =models.ForeignKey(BookedSlot, on_delete=models.CASCADE,)

    def __str__(self):
        return self.slot_name



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username =models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profiles/',null=True)
    phone_number =models.PositiveIntegerField()
    email =models.EmailField(max_length=100)
    location =models.ForeignKey(Location, on_delete=models.CASCADE)
    car_plate =models.CharField(max_length=20)
    car_model =models.CharField(max_length=20)
    parking_slot =models.ForeignKey(ParkSlot,on_delete=models.CASCADE)


    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        
    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()




