from django.shortcuts import render

# Create your views here.
def PPH21(request):
    content = {}
    content['title'] = 'PPH 21 Calculator'


    return render(request, 'ppn/ppn21.html', content)
def PPH22(request):
    content = {}
    content['title'] = 'PPH 22 Calculator'
    
    return render(request, 'ppn/ppn22.html', content)
def PPH23(request):
    content = {}
    content['title'] = 'PPH 23 Calculator'
    
    return render(request, 'ppn/ppn23.html', content)