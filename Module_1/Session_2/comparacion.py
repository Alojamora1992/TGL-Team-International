def igualdad(a, b):
    print(f"{a} es Igual a {b}:  {str(a == b)}")


igualdad(2, 3)
igualdad(2, 2)


def desigualdad(a, b):
    print(f"{a} es Desigual a {b}:  {str(a != b)}")


desigualdad(2, 3)
desigualdad(2, "String")

def mayor_que(a, b):
    print(f"{a} Mayor que {b}, {a > b}")

mayor_que(2, 3)
mayor_que(3, 2)

def menor_que(a, b):
    print(f"{a} Menor que {b}, {a < b}")

menor_que(2, 3)
menor_que(3, 2)


def mayor_igual(a, b):
    print(f"{a} es mayor o igual que {b} {a >= b}")

mayor_igual(2, 2)
mayor_igual(2, 19)

def menor_igual(a, b):
    print(f"{a} es menor o igual que {b} {a <= b}")

menor_igual(2, 2)
menor_igual(2, 19)