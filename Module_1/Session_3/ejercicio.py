"""Crear una aplicacion que le solicite al usuario el nombre y la edad del estudiante, luego crea un diccionario que representa al estudiante. Las claves del diccionario seran: "nombre", "edad" y "aprobado", el valor de las notas debe ser una lista de flotantes en un inicio vacia.

Luego se le solicitarea al usuario 5 notas( con valor de 1.0-5.0), las cuales deben ser agregadas al campo notas del diccionario del estudiante.

Finalmente, se debe calcular la nota promedio, si es mayor a 3, el campo aprobado debe ser true, en caso contrario se le asigna false."""


def student(name: str, edad: int):
    diccionario = {
        'nombre': name,
        'edad': edad,
        'notas': [],
        'aprobado': False
        }
    
    for i in range(5):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        diccionario['notas'].append(nota)
    
    promedio = sum(diccionario['notas'])/len(diccionario['notas'])
    
    if promedio >= 3:
        diccionario['aprobado'] = True
        print(diccionario)
    else:
        print(diccionario)

name = str(input("Ingrese el nombre del estudiante: "))
edad = int(input("Ingrese la edad del estudiante: "))   

student(name,edad)
    

