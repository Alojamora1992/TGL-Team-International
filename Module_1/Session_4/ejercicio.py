"""Crea una funcion que recibe una lista de numeros y devuelve un diccionarios con las siguientes claves y valores:
pares, impares y promedio.
EJ:
input [1,2,3,4,5]
output: {promedio: 3, pares: [2,4], impares: [1,3,5]}
"""

def list_compresion(lista):
    resultado = {
    'par': [x for x in lista if x % 2 == 0],
    'impar': [x for x in lista if x % 2 != 0],
    'promedio': sum(lista)/len(lista)
}
    print(resultado)

list_compresion([1,2,3,4,5,6])