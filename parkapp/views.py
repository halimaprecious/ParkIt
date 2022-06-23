from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect,get_object_or_404

from parkapp.models import Parkslot
from .forms import parkslotForm


# Create your views here.

# def home(request):

#     return render(request,'park/landingpage.html')


@login_required(login_url='/accounts/login/')
def signUp(request,parkslot_id):
 if request.method == 'POST':  
        form = parkslotForm(request.POST)  
        if form.is_valid():  
            email = form.cleaned_data['mimowaruguru@gmail.com']
            name = form.cleaned_data['Maureen']
        
            recipient.save()
        
        else:  
               form = parkslotForm()  
        return render(request, 'registration/registration_form.html', {'form': form})  




    # try:
    #     parkslot = ParkSlot.objects.get(id = parkslot_id)
    # except ObjectDoesNotExist:
    #     raise Http404()
    # return render(request,"registration/registration_form.html", {"parkslot":parkslot})

#        


# @login_required(login_url='/accounts/login/')
# def parkslot(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = parkslotForm(request.POST, request.FILES)
#         if form.is_valid():
#             park= form.save(commit=False)
#             park = current_user
#             park.save()
#         return redirect('home')

#     else:
#         form = parkslotForm()
#     return render(request, 'parkingslot.html', {"form": form})  



def parkit(request):
    parkslots =  Parkslot.objects.all()
    return render(request, 'park/parking.html', {'parkslots':parkslots})


def booked_slot(request, slot_id):
    slot = get_object_or_404(Parkslot, id=slot_id)
    request.user.profile.slot = slot
    request.user.profile.save()
    return redirect('parking', slot_id = slot.id)
    


# @login_required
# def join_hood(request, neighborhood_id):
#     neighborhood = get_object_or_404(NeighbourHood, id=neighborhood_id)
#     request.user.profile.neighbourhood = neighborhood
#     request.user.profile.save()
#     return redirect('neighbourhood', neighborhood_id = neighborhood.id)

# @login_required
# def leave_hood(request, neighborhood_id):
#     neighborhood = get_object_or_404(NeighbourHood, id=neighborhood_id)
#     request.user.profile.neighbourhood = None
#     request.user.profile.save()

