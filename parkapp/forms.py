from django import forms
from .models import *


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
