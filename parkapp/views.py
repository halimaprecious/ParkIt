from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Profile, User
from django.core.exceptions import ObjectDoesNotExist

def home(request):

    return render(request,'landingpage.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data['email']
            # recipient = Subscribers(name = username,email =email)
            # recipient.save()
            # send_welcome_email(username,email)
            messages.success(request, f'Successfully created account created ! Please log in to continue')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})