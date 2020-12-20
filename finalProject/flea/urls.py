from django.urls import path
from flea import views

app_name = 'flea'

urlpatterns = [
    path('',views.homepage),
    path('homepage/',views.homepage,name='homepage'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('product/',views.product,name='product'),
]
