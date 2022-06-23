from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required
# Create your views here.
 

def home(request):

    return render(request,'main/landingpage.html')



def park(request):
    return render(request,'parking.html')
