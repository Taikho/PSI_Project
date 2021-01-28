from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, DodatkoweInfo, Opinia, Uzytkownik, Zamowienie, Tranzakcja


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class DodatkoweInfoSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='product_detail')
    class Meta:
        model = DodatkoweInfo
        fields = ['__all__']


class OpiniaSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field='nazwa')
    uzytkownik = serializers.SlugRelatedField(queryset=Uzytkownik.objects.all(), slug_field='imie')
    class Meta:
        model = Opinia
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.teks_rec = validated_data('test_rec', instance.tekst_rec)
        instance.gwiazdy = validated_data('gwiazdy', instance.gwiazdy)
        instance.save()

        return instance


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    dodatkowe_info = serializers.SlugRelatedField(queryset=DodatkoweInfo.objects.all(), slug_field='rodzaj')
    opinie = OpiniaSerializer(many=True)

    class Meta:
        model = Product
        fields = ['url', 'id', 'nazwa', 'opis', 'cena', 'rozmiar', 'jest_dostepny', 'sukienka_cena',
                  'dodatkowe_info', 'opinie', 'rodzaj']
        read_only_fields = ('dodatkowe_info', 'opinia')


class UzytkownikSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Uzytkownik
        fields = ['url', 'id', 'imie', 'nazwisko', 'adres', 'nr_telefonu', 'adres_mailowy', 'czas_dodania']


class ZamowienieSerializer(serializers.HyperlinkedModelSerializer):
    klient = serializers.SlugRelatedField(queryset=Uzytkownik.objects.all(), slug_field='imie')
    product = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field='nazwa')
    class Meta:
        model = Zamowienie
        fields = ['url', 'klient', 'produkt', 'cena', 'data_utworzenia', 'ilosc', 'numer_pot']


class TranzakcjaSerializer(serializers.HyperlinkedModelSerializer):
    zamowienie = serializers.SlugRelatedField(queryset=Zamowienie.objects.all(), slug_field='cena')
    class Meta:
        model = Tranzakcja
        fields = ['url', 'potwierdzenie', 'platnosc', 'zamowienie']
