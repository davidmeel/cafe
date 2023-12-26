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
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')