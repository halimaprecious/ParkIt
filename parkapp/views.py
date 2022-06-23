from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required
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