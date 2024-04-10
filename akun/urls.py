from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import LandingPage, HomePage, LoginPage, LogoutPage, RegisterPage


urlpatterns = [
    path('', LandingPage, name="LandingPage"),
    path('home/', HomePage, name="HomePage"),
    path('accounts/login/', LoginPage, name="LoginPage"),
    path('accounts/logout/', LogoutPage, name="LogoutPage"),
    path('accounts/register/', RegisterPage, name="RegisterPage"),
]
