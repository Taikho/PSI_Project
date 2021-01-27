from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializers import UserSerializer
from .models import Product, Opinia, Uzytkownik
from .serializers import ProductSerializer, OpiniaSerializer, UzytkownikSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(jest_dostepny=False)
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.filter(jest_dostepny=False)
        return qs


class OpiniaViewSet(viewsets.ModelViewSet):
    queryset = Opinia.objects.all()
    serializer_class = OpiniaSerializer


class UzytkownikViewSet(viewsets.ModelViewSet):
    queryset = Uzytkownik.objects.order_by('imie')
    serializer_class = UzytkownikSerializer
