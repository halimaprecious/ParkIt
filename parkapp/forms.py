from django import forms
from .models import *
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  

class PayForSlotForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number', 'email', 'car_plate', 'parking_slot')


