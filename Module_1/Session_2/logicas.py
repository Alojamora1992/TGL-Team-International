def operacion_and(a, b):
    print("OPeracion and: ", a and b)

operacion_and(True, True)
operacion_and(False, True)
operacion_and(True, False)
operacion_and(False, False)

def operacion_or(a, b):
    print("Operacion or: ", a or b)

operacion_or(True, False)
operacion_or(True, False)
operacion_or(False, True)
operacion_or(False, False)
operacion_or(10, 1)


def operacion_not(a):
    print(f"Negacion de {a} -> {not a}")

operacion_not(True)

a = input("Ingresa el primer valor: ")
print(type(a))



def operaciones(a, b: int):
    a = int(a)
    b = str(b)
    print(f"tipo de dato de a = {type(a)} ... tipo de dato de b = {type(b)}")

operaciones(a, 20)