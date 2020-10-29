print("Hello World")

artykul = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz " \
          "pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków " \
          "później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował " \
          "się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, " \
          "a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na " \
          "komputerach osobistych, jak Aldus PageMaker "

imie = "Patryk"
nazwisko = "Reweda"

litera1 = imie[2]
litera2 = nazwisko[3]

print(litera1)
print(litera2)

liczba_liter1 = artykul.count(litera1)
liczba_liter2 = artykul.count(litera2)

print("W tekscie jest ", liczba_liter1, "liter " + litera1 + " oraz", liczba_liter2, "liter " + litera2)
