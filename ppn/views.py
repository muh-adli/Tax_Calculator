from django.shortcuts import render
from .forms import PPNForm

# Create your views here.
def PPN(request):

    Title = "PPN Calculator"

    form = PPNForm()

    content = {
        'title' : Title,
        'form' : form,
    }
    return render(request, 'ppn/ppn.html', content)