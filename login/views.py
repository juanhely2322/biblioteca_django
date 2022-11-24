from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def login_session(request):
    if request.method == "GET":
        return render(request, "login/login.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "login/login.html", {"form": AuthenticationForm,
                                                  "error": "Username o password is incorrect"})
        else:
            login(request, user)
            return redirect("libros")
  


def signup(request):
        if request.method == 'GET':
            return render(request, "login/singup.html", {'form': UserCreationForm})
        else:
            if request.POST["password1"] == request.POST["password2"]:
                # register user
                 try:
                    user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                    user.save()

                    login(request, user)

                    return redirect("libros")
                 except IntegrityError:
                    return render(request, "login/singup.html", {'form': UserCreationForm, "error": "User already exist "})
            else:
                return render(request, "login/singup.html", {'form': UserCreationForm, "error": "Password do not match"})
        
def logout_session(request):
    logout(request)
    return redirect("libros")