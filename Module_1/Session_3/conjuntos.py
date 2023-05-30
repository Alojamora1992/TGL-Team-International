#Definicion de un conjunto o set
set_1 = {2, 3, 4, 5, 5}
print(set_1)

#Adiccionar un elemento a un set, si ya existe no lo hace
set_1.add(6)
set_1.add(3)
print(set_1)

#Eliminar un elemento especifico de un set o conjunto 
set_1.remove(3)
print(set_1)

#Definicion de un set con la palabrareservada set
    
set_variable = set([1, 2, 3,4])
print(set_variable)


lista = [3, 3, 3, 4, 4]
print(lista)

#Metodo para eliminar elementos repetidos de una lista
set_duplicados = set([3, 3, 3, 4, 4])
print(set_duplicados)


set_1 = {2, 3, 4}
set_2 = {4, 5 , 6}

#Union de 2 sets, es como concatenar sin elementos repetidos
set_3 = set_1.union(set_2)
print(set_3)

#Elementos que estan en ambos conjuntos
set_4 = set_1.intersection(set_2)
print(set_4)
 
#Elementos que estan en el set-2 y no en en el set-1
set_5 = set_2.difference(set_1)

print(set_5)