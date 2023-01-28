from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sayhello(request):
    return render(request,'hello.html')
#def img(request):
    #return render(request,'img.html')
