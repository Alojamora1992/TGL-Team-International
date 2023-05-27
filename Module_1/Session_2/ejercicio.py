from aritmeticas import suma, resta, multiplicacion, division


def operaciones(a:int, b:int):
    print(f"Suma: {a} + {b} = {suma(a,b)}")
    print(f"Resta: {a} - {b} = {resta(a,b)}")
    print(f"Mult: {a} * {b} = {multiplicacion(a,b)}")
    print(f"Div: {a} / {b} = {division(a,b)}")
    
a = int(input("Digite el primer #: "))
b = int(input("Digite el segundo #: "))

operaciones(a,b)