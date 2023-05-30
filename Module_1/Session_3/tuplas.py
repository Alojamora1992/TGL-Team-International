#Una lista es inmutable
tupla = (2,3,4,5)
lista = [2,3,4,5]

lista[2] = "change"
print(lista)

tupla[2] = "change"
print(tupla)