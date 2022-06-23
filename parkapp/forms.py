from django import forms
from .models import *
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  

class PayForSlotForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number', 'email', 'car_plate')

class BookSlot(forms.ModelForm):
    class Meta:
        model = Parkslot
        exclude = ('image',)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
          'bio': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }

class parkslotForm(forms.ModelForm):
    class Meta:
        model = Parkslot
        exclude = ['publish_date']
