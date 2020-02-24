from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()

	        return redirect("home")
    else:
	    form = RegisterForm()

    return render(response, "registration/sign_up.html", {"form":form})


