from django.shortcuts import render
from django.http import HttpResponse
from flea import models
import datetime

# Create your views here.
def homepage(request):
    #if 'id' in request.session.keys():
    return render(request,'flea/homepage.html',locals())

def login(request):
    if request.method == "POST":
        username = request.POST.get("id")
        usertype = request.POST.get("type")
        password = request.POST.get("password")
        res = models.UserInfo.objects.filter(username=username,usertype=usertype,password=password).values()
        if len(res) == 1:
            request.session['id'] = res[0]["id"]
            request.session['username'] = res[0]["username"]
            if res[0]['usertype'] == "0":
                request.session['usertype'] = "admin"
            elif res[0]['usertype'] == "1":
                request.session['usertype'] = "seller"
            elif res[0]['usertype'] == "2":
                request.session['usertype'] = "buyer"
            return HttpResponse("1")
        else:
            return HttpResponse("0")
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
    else:
        return HttpResponse("0")

def adminPage(request):
    if request.method == "GET":
        userInfo = models.UserInfo.objects.all()
        products = models.Product.objects.all()
        return render(request,'flea/admin.html',locals())

def signout(request):
    request.session.flush()
    return HttpResponse("1")

def delete(request):
    if request.POST.get("type") == "0":
        id = request.POST.get("id")
        try:
            models.Cart.objects.filter(buyer=id).delete()
        except:
            pass
        try:
            res = models.Product.objects.filter(seller=id).value()
            for p in res:
                try:
                    models.AuctionInformation.objects.filter(product=p["id"]).delete()
                except:
                    continue
            models.Product.objects.filter(seller=id).delete()

        except:
            pass
        try:
            models.Product.objects.filter(buyer=id).delete()
        except:
            pass
        try:
            models.UserInfo.objects.filter(id=id).delete()
            return HttpResponse("1")
        except:
            return HttpResponse("0")
    else:
        return HttpResponse("0")

def modify(request):
    if request.POST.get("type") == "0":
        data = eval(request.POST.get("data"))
        try:
            for rolumn in data:
                inner = models.UserInfo.objects.get(id=rolumn[0])
                inner.username = rolumn[1]
                inner.password = rolumn[2]
                inner.email = rolumn[3]
                inner.usertype = rolumn[4]
                inner.save()
            return HttpResponse("1")
        except:
            return HttpResponse("0")

def sellerPage(request):
    return render(request,'flea/seller.html',locals())

def connectPage(request):
    return render(request,'flea/connect.html',locals())

def addProduct(request):
    id = request.session["id"]
    img = request.FILES.get("img")
    productName = request.POST.get("productname")
    price = request.POST.get("price")
    sellerName = request.POST.get("sellerName")
    sellerPhone = request.POST.get("sellerPhone")
    address = request.POST.get("address")
    selltype = request.POST.get("type")
    if selltype == "1":
        try:
            endtime = datetime.datetime.now() + datetime.timedelta(hours=int(request.POST.get("endtime")))
            models.Product.objects.create(productName=productName,picture=img,seller=id,price=price,sellType=selltype,sellerNumber=sellerPhone,sellerName=sellerName,tradePlace=address,endTime=endtime)
            return HttpResponse("1")
        except:
            return HttpResponse("0")
    else:
        try:
            models.Product.objects.create(productName=productName,picture=img,seller=id,price=price,sellType=selltype,sellerNumber=sellerPhone,sellerName=sellerName,tradePlace=address)
            return HttpResponse("1")
        except:
            return HttpResponse("0")