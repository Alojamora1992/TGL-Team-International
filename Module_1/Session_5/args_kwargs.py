def funcion_mixta(nombres, apellidos, *args, **kwargs):
    print(nombres)
    print(apellidos)
    print(args)
    print(kwargs)


funcion_mixta(1, 2, 3, nombre="Alejandro", edad="Velez")


funcion_mixta(1, 2, 3, nombre="Alejandro", edad="Velez")


lista = [1, 2, 3]

funcion_mixta(*lista)
funcion_mixta("Alejandro", "Velez", *lista)
