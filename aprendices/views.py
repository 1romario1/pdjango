from django.shortcuts import render
from . models import Aprendiz
# Create your views here.
# def aprendizlist(request):
#     return render(request,'aprendizlist.html')
def aprendizlist(request):
    get_aprendices=Aprendiz.objects.all()
    data={
        'get_aprendices':get_aprendices
    }
    return render(request,"aprendizlist.html",data)
