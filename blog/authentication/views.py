from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import RegisterForm
from templates import admin


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def signup(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()

	        return redirect("login")
    else:
	    form = RegisterForm()

    return render(response, "registration/sign_up.html", {"form":form})

# #redirect to admin panel
# def admin(request):
#     if request.user.is_superuser:
#     	return render(request,'/admin/index.html')
#     else:
#     	return redirect('/posts/')


def adminManage(request):
    if request.user.is_superuser:
    	return render(request,'admin.html')
    else:
    	return redirect('/posts/')
	


def user(request):
	users = User.objects.all()
	flag = User.is_superuser
	context = {
		'user':request.user,
		'users':users
	}
	return render(request,'user.html',context)

# #make user an admin
def adminMake(request, num):
	user = User.objects.get(id = num)
	user.is_superuser = True
	user.save()
	return redirect("user")

def block(request, num):
	user = User.objects.get(id = num)
	user.is_active = False
	user.save()
	return redirect("user")

# def adminManage(request):
# 	return redirect("admin")


def login(request):
	return render(request,'login.html')
