from django.shortcuts import render
from .models import Tusks

def tusks_home(request):
    tusk = Tusks.objects.all()
    tusk = Tusks.objects.order_by('date')
    return render(request,'tusks_home.html',{'tusk': tusk})

# Create your views here.
