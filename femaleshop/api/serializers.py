from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, DodatkoweInfo, Opinia, Uzytkownik


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class DodatkoweInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DodatkoweInfo
        fields = ['rodzaj', 'material']


class OpiniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinia
        fields = ['tekst_rec', 'gwiazdy']


class ProductSerializer(serializers.ModelSerializer):
    dodatkowe_info = DodatkoweInfoSerializer(many=False)
    opinie = OpiniaSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'nazwa', 'opis', 'cena', 'rozmiar', 'jest_dostepny', 'sukienka_cena',
                  'dodatkowe_info', 'opinie']

class UzytkownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uzytkownik
        fields = ['imie', 'nazwisko', 'adres', 'nr_telefonu', 'adres_mailowy', 'czas_dodania']
