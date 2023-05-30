# Usar python version >= 3.10

def funcion_desde_case():
    print("ENTRE a funcion desde case")

def funcion_con_match(code):
    match code:
        case 300:
            print("Entre a 300")
        case 200:
            print("Entre a 200")
        case 400:
            funcion_desde_case()
        case _:
            print("Case por defecto")


funcion_con_match(400)


def funcion_con_dict(code):
    diccionario = {
        300: "Entre a 300",
        200: "Entre a 200",
        400: "Entre a 400",
    }
    return diccionario[code]

try:
    print(funcion_con_dict(300))
except ValueError:
    print("Case por defecto")