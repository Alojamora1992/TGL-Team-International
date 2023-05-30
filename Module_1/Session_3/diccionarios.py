diccionario = {
    "nombre": "Carlos",
    "edad": "31",
    "trabajo": "developer",
    "mascotas": ["Nemesis"],
    "mascotas_completo": [
        {
            "nombre": "Nemesis",
            "edad": 2,
            "raza": "Doberman"
        }
    ]
}
#Imprimir todos los campos de un diccionario
print(diccionario)

#Imprimir las llaves o campos de los diccionarios
print(diccionario.keys())

#Imprimir los valores de las llaves de los diccionarios
print(diccionario.values())

#Imprimir tanto las keys y values del diccionario
print(diccionario.items())

#Imprimir un valor de una llave en especifico de forma insegura
print(diccionario["nombre"])

#Metodo mas seguro de acceder a algun valor de una llave en especifico, tiene caso por defedcto
print(diccionario.get("apellido", "No tiene apellido"))

#Adiccionar un campo a la lista mascotas
diccionario["mascotas"].append("Mascota2")

print(diccionario)

#Ir al key mascotas y obtener el valor del nombre de la primera mascota
print(diccionario["mascotas_completo"][0]["nombre"])

#Reasignar el valor de la llave nombre del diccionario
diccionario["nombre"] = "Carlos Posada"

print(diccionario)

#Actualizar los campos de un diccionario y agrega nuevos campos
diccionario.update({"nombre": "Carlos A. Posada"})
diccionario.update({"apellido": "Velez"})

print(diccionario)
