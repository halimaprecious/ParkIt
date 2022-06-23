from django import forms
from .models import *
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  


class BookSlotForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number','car_plate', 'car_model',)

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

class paymentForm(forms.ModelForm):
    class Meta:
        model= Payment
        exclude = ('user',)
