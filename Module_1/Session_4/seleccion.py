numero1 = 4
numero2 = 6

texto = "" # Se toma por defecto como vacio, por lo cual seria False

zero = 0 # Se toma por defecto como vacio, por lo cual seria False

none_ex = None # Se toma por defecto como vacio, por lo cual seria False

lista = [] # Se toma por defecto como vacio, por lo cual seria False

lista_engañosa = [[]] # Se toma como si estuviera con información por lo cual seria True

if not texto:
    print("El texto es un string vacio, error")

if numero1 >= 5 and numero2 <= 6:
    print("ENTRE")
elif numero1 == 4:
    print("Numero 4")
else:
    print("ENTRE ELSE")