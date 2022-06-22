from django.shortcuts import render

# Create your views here.
def park(request):
    return render(request,'parking.html')