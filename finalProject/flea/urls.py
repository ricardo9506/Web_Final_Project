from django.urls import path,re_path
from flea import views
from django.views.static import serve
from finalProject.settings import MEDIA_ROOT

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
    path('buyer/',views.buyerPage,name='buyer'),
    path('connect/',views.connectPage,name='connect'),
    path('addProduct/',views.addProduct,name='addProduct'),
    path('deal/',views.deal,name='deal'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
