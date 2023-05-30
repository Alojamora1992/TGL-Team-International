
#ciclo for de 4 iteraciones
def range_unico():
    for i in range(4):
        print(i)

#ciclo for con un rango en especifico
def range_multiple():
    for i in range(2, 10):
        print(i)
#ciclo for con paso de 2, 0,2,...,2n
def range_steps():
    for i in range(2, 10, 2):
        print(i)

#Iteracion de listas:

#iteracion con el valor de una lista
def iterar_lista():
    lista = ["Valor 1", "Valor 2", "Valor 3"]
    for valor in lista:
        print(valor)
    #Iteracion con la tupla indice valor, gracias a la palabra reservada enumerate
    for indice, valor in enumerate(lista):
        print(f"{indice} {valor}")

#Iteracion con el indice de una lista
def iterar_lista_range():
    lista = ["Valor 1", "Valor 2", "Valor 3"]
    for indice in range(len(lista)):
        print(lista[indice])

#Iteracion en diccionarios:

def iterar_diccionario():
    diccinario = {"Nombre": "Alejandro", "Apellido": "Velez", "Edad": 25}
    #Iteracion por clave forma1
    for clave in diccinario:
        print(diccinario[clave])
    #Iteracion por clave forma2
    for clave in diccinario.keys():
        print(clave)
    #Iteracion por valor forma1
    for valor in diccinario.values():
        print(valor)
    #Iteracion por la tupla clave,valor por medio del metodo items.
    for clave, valor in diccinario.items():
        print(f"{clave} {valor}")


#Condicional whiles:


def while_generico():
    numero = 1
    while numero < 5:
        print(numero)
        numero += 1

def do_while():
    numero = 1
    while True:
        if numero == 5:
            break
        print(numero)
        numero += 1
    print("Finalice")


def continue_list():

    lista = ["Valor 1", "valor 2", "Valor 3"]

    for valor in lista:
        if valor == "valor 2":
            continue
        print(valor)

continue_list()