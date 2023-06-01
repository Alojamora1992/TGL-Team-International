class Animal:

    def __init__(self, color):
        self.color = color

    def color_animal(self):
        print(f"Soy de color {self.color}")

#Los valores por defecto tambien se heredan ej: ladra
class Perro:
    ladra = True

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola me llamo {self.nombre}, y tengo {self.edad} años")

#Si tenemos multiple herencia, como en este caso, no utilizamos el metodo super, en vez de ello, utilizamos el nombre de la clase y el metrodo a heredar.
class PerroGuia(Perro, Animal):

    def __init__(self, nombre, raza, edad, entrenado):
        Perro.__init__(self, nombre, edad)
        Animal.__init__(self, "Rojo")
        self.raza = raza
        self.entrenado = entrenado

    def validar_entrenado(self):
        if self.entrenado:
            print("Estoy entrenado")
        else:
            print("No estoy entrenado")

    def perro_ladra(self):
        print(f"el perro ladra {self.ladra}")


perro = PerroGuia("Juan", "Border collie", "2 años", True)

perro.saludar()
perro.validar_entrenado()
perro.color_animal()
perro.perro_ladra()