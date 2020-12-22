from django.urls import path
from flea import views

app_name = 'flea'

urlpatterns = [
    path('',views.homepage),
    path('homepage/',views.homepage,name='homepage'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('product/',views.product,name='product'),
    path('search/',views.search,name='search'),
    path('checkId/',views.checkId,name='checkId'),
    path('admin/',views.adminPage,name='admin'),
    path('signout/',views.signout,name='signout'),
    path('delete/',views.delete,name="delete"),
    path('modify/',views.modify,name="modify"),
    path('seller/',views.sellerPage,name='seller'),
    path('connect/',views.connectPage,name='connect'),
    path('addProduct/',views.addProduct,name='addProduct'),
]
