from django.shortcuts import render

from .models import *

def home(request):
    phones = Phone.objects.all()
    context = {
        "phones":phones
    }
    return render(request, "phones/home.html", context)

def phone_details(request, pk):
    phone = Phone.objects.get(pk=pk)
    context = {
        "phone":phone
    }
    return render(request, "phones/phone_details.html", context)