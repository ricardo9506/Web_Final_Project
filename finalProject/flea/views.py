from django.shortcuts import render
from django.http import HttpResponse
from flea import models
import datetime,pytz
utc=pytz.UTC

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
        product = models.Product.objects.filter(id=productId).values()[0]
        try:
            endtime = product["endTime"].__format__('%Y/%m/%d %H:%M:%S')
        except:
            pass
        return render(request,'flea/product.html',locals())
    else:
        return render(request,'flea/homepage.html',locals())

def search(request):
    if request.method == "POST":
        searchType = request.POST.get("type")
        if searchType == "name":
            res = models.Product.objects.filter(productName__contains=request.POST.get("key1")).values()
            result = list()
            for r in res:
                l = list()
                for k in r.keys():
                    if k == "uploadTime":
                        l.append(r["uploadTime"].__format__('%Y/%m/%d %H:%M:%S'))
                        continue
                    elif k == "endTime":
                        if r["endTime"] == None:
                            l.append("null")
                        else:
                            l.append(r["endTime"].__format__('%Y/%m/%d %H:%M:%S'))
                    else:
                        l.append(r[k])
                if r["sellType"] == "0":
                    if r["buyer"] == -1:
                        l.append("Selling")
                    else:
                        l.append("Sold")
                else:
                    if utc.localize(r["endTime"]) > utc.localize(datetime.datetime.now()):
                        l.append("Bidding")
                    else:
                        l.append("End Bidded")
                result.append(l)
            return HttpResponse(str(result))
        else:
            res = models.Product.objects.filter(price__range=[request.POST.get("key1"),request.POST.get("key2")]).values()
            result = list()
            for r in res:
                l = list()
                for k in r.keys():
                    if k == "uploadTime":
                        l.append(r["uploadTime"].__format__('%Y/%m/%d %H:%M:%S'))
                        continue
                    elif k == "endTime":
                        if r["endTime"] == None:
                            l.append("null")
                        else:
                            l.append(r["endTime"].__format__('%Y/%m/%d %H:%M:%S'))
                    else:
                        l.append(r[k])
                if r["sellType"] == "0":
                    if r["buyer"] == -1:
                        l.append("Selling")
                    else:
                        l.append("Sold")
                else:
                    if utc.localize(r["endTime"]) < utc.localize(datetime.datetime.now()):
                        l.append("Bidding")
                    else:
                        l.append("End Bidded")
                result.append(l)
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
        feedback = models.FeedBackInformation.objects.all()
        return render(request,'flea/admin.html',locals())

def signout(request):
    request.session.flush()
    return HttpResponse("1")

def delete(request):
    if request.POST.get("type") == "0":
        id = int(request.POST.get("id"))
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
    elif request.POST.get("type") == "1":
        id = request.POST.get("id")
        try:
            models.Product.objects.filter(id=int(id)).delete()
            modeles.AuctionInformation.objects.filter(product=int(id)).delete()
            return HttpResponse("1")
        except:
            return HttpResponse("1")
    else:
        return HttpResponse("0")

def modify(request):
    if request.POST.get("type") == "0":
        data = eval(request.POST.get("data"))
        try:
            for rolumn in data:
                models.UserInfo.objects.filter(id=rolumn[0]).update(username=rolumn[1],password=rolumn[2],email=rolumn[3],usertype=rolumn[4])
            return HttpResponse("1")
        except:
            return HttpResponse("0")
    elif request.POST.get("type") == "1":
        data = eval(request.POST.get("data"))
        try:
            for rolumn in data:
                models.Product.objects.filter(id=int(rolumn[0])).update(productName=rolumn[1],tradePlace=rolumn[2])
            return HttpResponse("1")
        except:
            return HttpResponse("0")

def sellerPage(request):
    products = models.Product.objects.filter(seller=int(request.session["id"])).values()
    auction = models.AuctionInformation.objects.all().values()
    users = models.UserInfo.objects.all().values()
    return render(request,'flea/seller.html',locals())

def buyerPage(request):
    orders = models.Product.objects.filter().values()
    auctions = models.AuctionInformation.objects.filter(bidder=int(request.session["id"])).values()
    cart = models.Cart.objects.filter(buyer=int(request.session["id"])).values()
    return render(request,'flea/buyer.html',locals())

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

def deal(request):
    if request.POST.get("type") == "0":#add to cart
        try:
            productid = int(request.POST.get("id"))
            models.Cart.objects.get_or_create(buyer=request.session['id'],product=productid)
            return HttpResponse("1")
        except:
            return HttpResponse("0")
        return HttpResponse("2")

    elif request.POST.get("type") == "1":#buy
        try:
            productid = int(request.POST.get("id"))
            models.Product.objects.filter(id=productid).update(buyer=request.session['id'])
            return HttpResponse("1")
        except:
            return HttpResponse("0")
        return HttpResponse("2")
    elif request.POST.get("type") == "2":
        try:
             productid = int(request.POST.get("id"))
             price = int(request.POST.get("price"))
             models.AuctionInformation.objects.get_or_create(product=productid,bidder=request.session['id'],price=price)
             models.Product.objects.filter(id=productid).update(price=price,buyer=request.session['id'])
             return HttpResponse("1")
        except:
            return HttpResponse("0")
        return HttpResponse("2")
    elif request.POST.get("type") == "3":
        try:
            name = request.POST.get("name")
            email = request.POST.get("email")
            usertype = request.POST.get("utype")
            inner = request.POST.get("inner")
            models.FeedBackInformation.objects.create(name=name,email=email,usertype=usertype,inner=inner)
            return HttpResponse("1")
        except:
            return HttpResponse("0")