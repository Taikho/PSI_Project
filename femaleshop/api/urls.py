from django.conf.urls import path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
path('products', views.ProductList.as_view(), name=views.ProductList.name),
path('products/<int:pk>', views.ProductDetail.as_view(), name=views.ProductDetail.name),
path('users', views.UserList.as_view(), name=views.UserList.name),
path('users/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
path('klient', views.UzytkownikList.as_view(), name=views.UzytkownikList.name),
path('klient/<int:pk>', views.UzytkownikDetail.as_view(), name=views.UzytkownikDetail.name),
path('opinia', views.OpiniaList.as_view(), name=views.OpiniaList.name),
path('opinia/<int:pk>', views.OpiniaDetail.as_view(), name=views.OpiniaDetail.name),
path('opinia', views.OpiniaList.as_view(), name=views.OpiniaList.name),
path('opinia/<int:pk>', views.OpiniaDetail.as_view(), name=views.OpiniaDetail.name),
path('zamowienie', views.ZamowienieList.as_view(), name=views.ZamowienieList.name),
path('zamowienie/<int:pk>', views.ZamowienieDetail.as_view(), name=views.ZamowienieDetail.name),
path('tranzakcja', views.TranzakcjaList.as_view(), name=views.TranzakcjaList.name),
path('tranzakcja/<int:pk>', views.TranzakcjaDetail.as_view(), name=views.TranzakcjaDetail.name),
path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
