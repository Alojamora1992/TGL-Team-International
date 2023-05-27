# TIPOS DE DATOS: 

# int   para entero
# float para numeros con decimales
# str   para cadenas de texto
# bool  para datos true o false
# list  para arreglos
# dict  para dictionarios o jsons

def suma(a: int, b: int):
    return a + b

#print(f"suma: {10} + {20} = {suma(10, 20)}")


def resta(a: int, b: int):
    return a - b

#print(f"resta: {4} - {10} = {resta(4, 10)}")

def multiplicacion(a: int, b: int):
    return a * b

#print(f"mult: {10} * {2} = {multiplicacion(10, 2)}")

def division(a: int, b: int):
    return int(a / b)

#print(f"div:  {20} / {2} = {division(20, 2)}")

def modulo(a: int, b: int):
    return a % b

#print(f"res:  {10} % {4} = {modulo(10, 4)}")

def potencia(a: int, b: int):
    return a ** b

#print(f"pot:  {2} ** {3} = {potencia(2, 3)}")