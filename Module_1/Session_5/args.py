#Puedo acceder y manipular sus valores por su indice.
def primeros_args1(*args):
    operacion = args[0] + sum(args[2])
    print(operacion)

lista_args1 = [2,"Hola", [1,2,3],"Adios"]
primeros_args1(lista_args1)    

#con el *Imprime tuplas, sin el * imprime un solo valor 
def primeros_args2(*args):
    print(args)
    
lista_args2 = ["Lista", "de", "Args"]
primeros_args2(*lista_args2)

