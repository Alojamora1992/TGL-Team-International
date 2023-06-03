def funcion_parametro():
    print("soy la funcion parametro")

def primeros_kwargs(primer_parametro,**kwargs):
    print(kwargs)
    
    for key, value in kwargs.items():
        print(key,value)
        if callable(value):
            value()
    print(primer_parametro)
    
diccionario = {"Hola": "persona", "Edad": 23, "funcion": funcion_parametro}

primeros_kwargs(primer_parametro= "primero",**diccionario)
primeros_kwargs(primer_parametro= "primero",hola = "persona", Edad = 23, funcion = funcion_parametro)