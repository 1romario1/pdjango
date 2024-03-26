from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     return HttpResponse('<h1>REPASO BACKEND ADSO 2560664B</h1>')

def home(request):
    return render(request,'home.html')
