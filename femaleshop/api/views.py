from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse

from api.serializers import UserSerializer
from .models import Product, Opinia, Uzytkownik, Zamowienie, Tranzakcja
from .serializers import ProductSerializer, OpiniaSerializer, UzytkownikSerializer, ZamowienieSerializer, \
    TranzakcjaSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 6


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = IsAuthenticatedOrReadOnly
    pagination_class = LargeResultsSetPagination
    serializer_class = ProductSerializer
    name = 'produkt-lista'
    filter_fields = ['nazwa', 'cena', 'rozmiar', 'jest_dostepny']
    search_fields = ['nazwa', 'rozmiar', 'cena']
    ordering_fields = ['nazwa', 'cena']


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = IsAuthenticatedOrReadOnly
    name = 'produkt-detail'

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = IsAuthenticated
    name = 'user-list'


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class UzytkownikList(generics.ListCreateAPIView):
    queryset = Uzytkownik.objects.all()
    serializer_class = UzytkownikSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = IsAuthenticated
    name = "uzytkownik-list"
    filterset_fields = ['imie', 'nazwisko', 'adres', 'nr_telefonu', 'adres_mailowy']
    search_fields = ['imie', 'nazwisko', 'adres', 'nr_telefonu']
    ordering_fields = ['imie', 'nazwisko']


class UzytkownikDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'uzytkownik-detail'
    queryset = Uzytkownik.objects.all()
    serializer_class = UzytkownikSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = IsAuthenticated

    def post(self, request):
        serializer = UzytkownikSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OpiniaList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = OpiniaSerializer
    filterset_fields = ['gwizady', 'products']
    authentication_classes = (TokenAuthentication,)
    permission_classes = IsAuthenticatedOrReadOnly
    name = 'opinia-list'


class OpiniaDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'opinia-detail'
    queryset = Opinia.objects.all()
    serializer_class = OpiniaSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = IsAuthenticatedOrReadOnly

    def post(self, request):
        serializer = OpiniaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ZamowienieList(generics.ListCreateAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = IsAuthenticatedOrReadOnly
    name = "zamowienie-list"
    filterset_fields = ['klient', 'produkt', 'cena', 'data_utworzenia']


class ZamowienieDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'zamowienie-detail'
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = IsAuthenticatedOrReadOnly


class TranzakcjaList(generics.ListCreateAPIView):
    queryset = Tranzakcja.objects.all()
    serializer_class = TranzakcjaSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = IsAuthenticatedOrReadOnly
    name = "tranzakcja-list"
    ordering_fields = ['potwierdzenie']


class TranzakcjaDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'tranzakcja-detail'
    queryset = Tranzakcja.objects.all()
    serializer_class = TranzakcjaSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = IsAuthenticatedOrReadOnly


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'products': reverse(ProductList.name, request=request),
                         'users': reverse(UserList.name, request=request),
                         'klient': reverse(UzytkownikList.name, request=request),
                         'opinia': reverse(OpiniaList.name, request=request),
                         'zamowienie': reverse(ZamowienieList.name, request=request),
                         'Tranzakcja': reverse(TranzakcjaList.name, request=request),

                         })
