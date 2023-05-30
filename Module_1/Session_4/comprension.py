def lista_comprension():
    lista_alcuadrado = [a**2 for a in range(5)] # Comprension de listas
    print(lista_alcuadrado)
    lista = []
    for a in range(5): # Forma completa
        lista.append(a**2)
    print(lista)


def if_lista_comprension():
    lista_pares = [a for a in range(6) if a%2 == 0]
    print(lista_pares)

    lista = []
    for a in range(6):
        if a%2 == 0:
            lista.append(a)

    print(lista)


def dic_comprension():
    dict_alcuadrado = {a: a**2 for a in range(5)}
    print(dict_alcuadrado)

    diccionario = {}
    for a in range(5):
        diccionario.update({a: a**2})
    print(diccionario)


def if_dic_comprension():
    dict_alcuadrado = {a: a**2 for a in range(5) if a == 2}
    print(dict_alcuadrado)

# dic_comprension()


print(max([2, 3, 4, 5]))
print(min([2, 3, 4, 5]))