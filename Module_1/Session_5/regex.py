import re

def re_match_search(cadena: str):

    if re.match("gato", cadena):
        print("Se encontro gato match")

    if re.search("ato", cadena):
        print("Se encontro ato en search")



re_match_search("gato en el tejado")



def re_findall(cadena):
    lista_emails = re.findall("\S+@\S+", cadena)
    print(lista_emails)

re_findall("Alejandro-243@hotmail.com , velez@m.com , Hola")

def re_sub(cadena):
    nueva_cadena = re.sub("gatos", "perros", cadena)
    print(nueva_cadena)

re_sub("Los gatos brincan en el tejado siguiendo gatos")


def buscar_numeros(cadena):
    numeros = re.findall(r"[-+]?\d+", cadena)
    print(numeros)


buscar_numeros("Cadena 10 numeros debe encontrar 1 vez -1")


def buscar_email(cadena):
    correos = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', cadena)
    print(correos)

buscar_email("Por favor, contactar a ana@example.com o a juan@example.org para más información.")
