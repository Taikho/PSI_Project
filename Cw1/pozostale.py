lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = []

lista2.insert(0, lista.pop(5))
lista2.insert(1, lista.pop(5))
lista2.insert(2, lista.pop(5))
lista2.insert(3, lista.pop(5))
lista2.insert(4, lista.pop(5))

lista3 = lista + lista2
lista3.insert(0, 0)
lista3.sort(reverse=True)

print(lista)
print(lista2)
print(lista3)
