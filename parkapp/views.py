from django.shortcuts import render,redirect
from django import forms
from django.contrib.auth import login, authenticate
from .forms import PayForSlotForm
from .models import *

from django.contrib.auth.decorators import login_required
# Create your views here.
def park(request):
    return render(request,'parking.html')
 

def home(request):
    return render(request,'main/landingpage.html')

def pay(request):
      if request.method == 'POST':
        form = PayForSlotForm(request.POST, request.FILES)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.admin = request.user
            payment.save()
            return redirect('paynow')
        else:
            form = PayForSlotForm()
            profile = Profile.objects.all()
        return render(request, 'payment.html', {'form': form, 'profile': profile})
