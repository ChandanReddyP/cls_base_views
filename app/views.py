from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *

def strbyfbv(request):
    return HttpResponse("This is function based view")

class StrbyCbv(View):
    def get(self,request):
        return HttpResponse("This is an class based view")
    


def fbvfile(request):
    return render(request,'fbvfile.html')

class Cbvfile(View):
    def get(self,request):
        return render(request,'Cbvfile.html')
    


def isbyfbv(request):
    ESFO=StudentMF()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=StudentMF(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Created')
        else:
            return HttpResponse("Invalid")
    return render(request,'isbyfbv.html',d)

class Isbycbv(View):
    def get(self,request):
        ESFO=StudentMF()
        d={'ESFO':ESFO}
        return render(request,'Isbycbv.html',d)
    def post(self,request):
        SFDO=StudentMF(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('created')
        else:
            return HttpResponse('invalid')