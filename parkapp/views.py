from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from .mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
# Create your views here.
 

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

#create your views here
def getAccessToken(request):
    consumer_key ='UPaUKccind4sSEGwBZPCA7q4pAB5ZzIw'
    consumer_secret = 'MDkX4fbCL073PspR'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)


def lipa_na_mpesa_online(request):
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
    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse('success')
