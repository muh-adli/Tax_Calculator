from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from views import *

urlpatterns = [
    path('pph21/', PPH21, name="PPH21"),
    path('pph22/', PPH22, name="PPH22"),
    path('pph23/', PPH23, name="PPH23"),
]