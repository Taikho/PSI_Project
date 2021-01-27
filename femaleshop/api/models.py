from django.db import models


class DodatkoweInfo(models.Model):
    RODZAJE = {
        (0, 'Nieznany'),
        (1, 'Sukienka'),
        (2, 'Suknia'),
        (3, 'Spodniczka'),
        (4, 'Zakiet'),
        (5, 'Spodnie'),

    }

    rodzaj = models.IntegerField(choices=RODZAJE, default=0)
    material = models.TextField(max_length=256)


class Product(models.Model):
    nazwa = models.CharField(max_length=32)
    opis = models.TextField(max_length=256)
    cena = models.IntegerField()
    rozmiar = models.CharField(max_length=32)
    jest_dostepny = models.BooleanField(default=False)
    dodatkowe_info = models.OneToOneField(DodatkoweInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.sukienka_cena()

    def sukienka_cena(self):
        return self.nazwa + "(" + str(self.cena) + " )"


class Opinia(models.Model):
    tekst_rec = models.TextField(default='')
    gwiazdy = models.IntegerField(default=0)
    produkt = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='opinie')


class Uzytkownik(models.Model):
    imie = models.CharField(max_length=50, null=False)
    nazwisko = models.CharField(max_length=50, null=False)
    adres = models.TextField(blank=True, null=True)
    nr_telefonu = models.CharField(max_length=12, null=True, blank=True)
    adres_mailowy = models.EmailField(max_length=45, null=False)
    czas_dodania = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.imie + "(" + str(self.adres_mailowy) + ")"
