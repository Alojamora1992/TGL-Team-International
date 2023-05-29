# Imprimir una lista que tiene varios tipos de datos
lista_1 = [1, 2, "Texto", ["Otra lista", 2, 4]]
print(lista_1)
print(type(lista_1)) # obtenemos el tipo de dato


#Imprimir una lista que se le agrega un string al final de la lista con el metodo append
lista_append = [5, 2, 34]
lista_append.append("Final")
print(lista_append)

#Remover un elemento en especifico de la lista
lista_remove = [5, 6, 7, 76]
lista_remove.remove(6)
print(lista_remove)

#Organizar la lista de orden ascendente(por defecto)
lista_sort = [753, 6, 5, 23, 321, ]
lista_sort.sort()
print(lista_sort)

#Organizar una lista en orden descendnte
lista_sort.sort(reverse=True)
print(lista_sort)

lista_sort = ["B", "Manuela", "Pepito", "A"]
lista_sort.sort(reverse=True)
print(lista_sort)

#Invertir una lista
lista_reverse = ["B", "Manuela", "Pepito", "A"]
lista_reverse.reverse()
print(lista_reverse)

#Obtener el indice de un valor en especifico de una lista y cuantas veces esta 
lista = ["B", "Manuela", "Pepito", "A", "Ultimo"]
print(lista.index("B"))
print(lista.count("B"))

#Imprimir la longitud de la lista y la suma de sus elementos
print(len(lista))
print(sum([5, 6, 3]))

#Imprimir una parte parcial de la lista de [0:3]
print(lista[0:3])

#Imprimir el ultimo elemento de la lista
print(lista[-1])
print(lista[len(lista) - 1])

#Eliminar un elemento con un indice especifico de una lista
lista.pop(2)
print(lista)