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
        username = request.POST.get("id")
        usertype = request.POST.get("type")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            models.UserInfo.objects.create(username=username,usertype=usertype,email=email,password=password)
            return HttpResponse("1")
        except:
            return HttpResponse("0")
    elif request.method == "GET":
        return render(request,'flea/signup.html',locals())

def product(request):
    if "id" in request.GET:
        productId = request.GET.get("id")
        return render(request,'flea/product.html',locals())
    else:
        return render(request,'flea/homepage.html',locals())

def search(request):
    if request.method == "POST":
        searchType = request.POST.get("type")
        if searchType == "name":
            res = models.Product.objects.filter(productName__contains=request.POST.get("key1"))
            result = list()
            for r in res:
                result.append(r)
            return HttpResponse(str(result))
        else:
            res = models.Product.objects.filter(productName__range=[request.POST.get("key1"),request.POST.get("key2")])
            result = list()
            for r in res:
                result.append(r)
            return HttpResponse(str(result))

def checkId(request):
    if request.method == "POST":
        id = request.POST.get("id")
        userType = request.POST.get("type")
        res = models.UserInfo.objects.filter(username=id,usertype=userType)
        if len(res) == 0:
            return HttpResponse("1")
        else:
            return HttpResponse("0")