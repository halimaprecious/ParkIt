
from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username =models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profiles/',null=True)
    phone_number =models.PositiveIntegerField(default=0)
    email =models.EmailField(max_length=100)
    car_plate =models.CharField(max_length=20)
    car_model =models.CharField(max_length=20)
  

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




class Parkslot(models.Model):
    user = models.ForeignKey( Profile, blank=True , null=True, on_delete=models.CASCADE)
    slot_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', default='default.jpeg')
   

    def create_parkslot(self):
        self.save()
        
    def delete_parkslot(self):
        self.delete()
        
    @classmethod
    def find_parkslot(cls,id):
        search = cls.objects.get(id = id)
        return  search
    

    def __str__(self):
        return self.slot_name


class Payment(models.Model):
    user = models.ForeignKey( Profile, blank=True , null=True, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=100)
    phone_number =models.PositiveIntegerField(default=254799735661)

    def __str__(self):
        return f'{self.name} payment'

    def save_payment(self):
        self.save()

    def delete_payment(self):
        self.delete()



