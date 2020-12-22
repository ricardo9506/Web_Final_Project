from django.db import models

# Create your models here.
class UserInfo(models.Model):

    id = models.AutoField(primary_key=True,verbose_name='id')
    username = models.CharField(max_length=30,verbose_name='username')
    password = models.CharField(max_length=30,verbose_name='password')
    email = models.CharField(max_length=30,verbose_name='email')
    usertype = models.CharField(max_length=10,verbose_name='usertype')

    def __str__(self):
        return '%s %s'%(self.username,self.usertype)

    class Meta:
        verbose_name = 'user information'
        verbose_name_plural = 'users'


class Product(models.Model):

    id = models.AutoField(primary_key=True,verbose_name='id')
    productName = models.CharField(max_length=20,verbose_name='productName')
    picture = models.FileField(upload_to='productImage/',verbose_name='pictureName',null=True)
    seller = models.IntegerField(verbose_name='seller')
    buyer = models.IntegerField(verbose_name='buyer',default=-1)
    price = models.IntegerField(verbose_name='price')
    sellType = models.CharField(max_length=10,verbose_name='sellType')
    sellerNumber = models.CharField(max_length=20,verbose_name='sellerNumber')
    sellerName = models.CharField(max_length=20,verbose_name='sellerName')
    tradePlace = models.CharField(max_length=50,verbose_name='tradePlace')
    uploadTime = models.DateTimeField(auto_now=False, auto_now_add=True)
    endTime = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)

    def __str__(self):
        return self.productName

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class AuctionInformation(models.Model):

    id = models.AutoField(primary_key=True,verbose_name='id')
    product = models.IntegerField(verbose_name='product')
    bidder = models.IntegerField(verbose_name='bidder')
    price = models.IntegerField(verbose_name='price')
    uploadTime = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return '%s %s'%(self.product,self.price)

    class Meta:
        verbose_name = 'AuctionInformation'
        verbose_name_plural = 'AuctionInformations'


class FeedBackInformation(models.Model):

    id = models.AutoField(primary_key=True,verbose_name='id')
    name = models.CharField(max_length=20,verbose_name='name')
    email = models.CharField(max_length=30,verbose_name='email')
    usertype = models.CharField(max_length=10,verbose_name='usertype')
    inner = models.CharField(max_length=200,verbose_name='inner')

    def __str__(self):
        return self.inner

    class Meta:
        verbose_name = 'FeedBackInformation'
        verbose_name_plural = 'FeedBackInformations'


class Cart(models.Model):

    id = models.AutoField(primary_key=True,verbose_name='id')
    buyer = models.IntegerField(verbose_name='buyer')
    product = models.IntegerField(verbose_name='product')
    uploadTime = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return '%s %s'%(self.product,self.buyer)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'