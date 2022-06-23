from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate

from parkapp.forms import BookSlotForm
from .models import *

from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from parkapp.models import Parkslot

# mpesa 
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from .mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.forms.models import model_to_dict
from django.http import JsonResponse
# Create your views here.
def park(request):
    return render(request,'parking.html')
 

def home(request):
    return render(request,'main/landingpage.html')


@login_required(login_url='/accounts/login/')
def user_profiles(request):
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('profile')
        
    else:
        form = ProfileUpdateForm()
    
    return render(request, 'registration/profile.html', {"form":form})

def getAccessToken(request):
    consumer_key ='UPaUKccind4sSEGwBZPCA7q4pAB5ZzIw'
    consumer_secret = 'MDkX4fbCL073PspR'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)


def lipa_na_mpesa_online(request):
    # profile = Profile.objects.filter(user=request.user).first()
    # phone_number = profile.phone_number
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": 254799735661,  # replace with your phone number to get stk push
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": 254799735661,  # replace with your phone number to get stk push
        "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        "AccountReference": "PARKIT",
        "TransactionDesc": "Testing stk push"
    }
  
    
def park(request):
    parkslots =  Parkslot.objects.all()
    return render(request,'parking.html',{'parkslots':parkslots})


def book(request):
    form = BookSlotForm(request.POST)
    if request.method == 'POST':
        form = BookSlotForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('payment')

    return render(request, 'book.html', {'form':form})


    

def payment(request):
    current_user = request.user
    if request.method == 'POST':
        form = paymentForm(request.POST, request.FILES)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = current_user
            payment.save()

        return redirect('bookspace')

    else:
        form = paymentForm()
    return render(request, 'payment.html', {"form": form})

