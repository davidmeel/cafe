from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.


def home(request):
    features = Mode.objects.all()
    menus = MenuModel.objects.all()
    context = {
        'features' : features,
        'menus' : menus
    }
    return render(request, 'index.html', context=context)




def reservation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        reserve = ReservationModel.objects.create(
            name=name,
            email=email,
            message=message,
        )
        reserve.save()
        return redirect('home')