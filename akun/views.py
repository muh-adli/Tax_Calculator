from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def LandingPage(request):
    html = "akun/LandingPage.html"
    return render(request, html)

def LoginPage(request):
    if request.method == 'POST':
        # print("masuk post")
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        # print(password, username)
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            messages.info(request, "Credentials Valid")
            return redirect('HomePage')
        else:
            # print("invalid")
            messages.error(request, "Invalid Credentials")
            return render(request, "LoginPage.html")
    else:
        # print("tidak post")
        return render(request, "akun/LoginPage.html")

@login_required()
def LogoutPage(request):
    logout(request)
    messages.warning(request, "Logout")
    return redirect('LoginUser')

def RegisterPage(request):
    if request.method == 'POST':
        # print("masuk post")
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        Passwordagain = request.POST.get('Passwordagain')
        Email = request.POST.get('Email')
        # print(Password, Username)
        # print(user)
        if Username and Password and Email is not None:
            if Password == Passwordagain:
                user = User.objects.create_user(username=Username,
                                                email=Email,
                                                password=Password)
                user.save()
                messages.info(request, "Credentials Created")
                return redirect('LandingPage')
            else:
                messages.info(request, "Password didn't match")
                return redirect('LandingPage')
        else:
            # print("invalid")
            messages.error(request, "Invalid Data")
            return redirect('LandingPage')
    # print("tidak post")
    else:
        return render(request, "akun/RegisterPage.html")

@login_required()
def HomePage(request):
    Title = 'Homepage'
    context = {'Title':Title}
    return render(request, "akun/HomePage.html", context)