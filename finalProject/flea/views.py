from django.shortcuts import render
from django.http import HttpResponse
from flea import models

# Create your views here.
def homepage(request):
    #if 'id' in request.session.keys():
    return render(request,'flea/homepage.html',locals())

def login(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        return render(request,'flea/login.html',locals())

def signup(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        return render(request,'flea/signup.html',locals())

def product(request):
    if "id" in request.GET:
        productId = request.GET.get("id")
        print(productId)
        return render(request,'flea/product.html',locals())
    else:
        return render(request,'flea/homepage.html',locals())