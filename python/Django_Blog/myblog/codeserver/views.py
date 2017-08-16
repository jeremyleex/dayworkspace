from django.shortcuts import render
from django.http import HttpResponse
from .models import codeserver
# Create your views here.

def codeserverIndex(request,key):
    
    codedata = codeserver.objects.get(key=key)
    print(codedata)
    print(codedata.code)
    return render(request,"codeserverindex.html",{'code':codedata.code,'usr':codedata.usr})