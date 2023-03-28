from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def about(request):
    return render(request, "about.html")

def home(request):
    return render(request, "home.html")

def password(request):
    chars = list("abcdefghijklmnopqrstuvwxyz")
    upper_chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    special = list("!@#$%&/()=?¿><_-+")
    numbers = list("0123456789")
    pass_gen = ""
    
    lenght = int(request.GET.get('lenght'))
    
    if request.GET.get('uppercase'):
        chars.extend(upper_chars)
    
    if request.GET.get('special'):
        chars.extend(special)
        
    if request.GET.get('numbers'):
        chars.extend(numbers)
    
    for x in range(lenght):
        pass_gen += random.choice(chars)
    
    return render(request, "password.html", {
        "password": pass_gen
    })