# Asignacion simple

a = 2
#Variable global
SOY_GLOBAL = "SOY GLOBAL"

print(a)

# Asignacion multiple
b, c, d = 7, 3.233, "String"

print(b)
print(c)
print(d)

# asignar resultados de funciones

def retornar():
    return "Retorne un valor"


def variables_global():
    local = "Soy local"
    SOY_GLOBAL = "CAMBIO DE VALOR"
    print(SOY_GLOBAL)

retornado = retornar()

print(retornado)
print(variables_global())
print(SOY_GLOBAL)