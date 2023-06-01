class Perro:
    ladra = True
    _protegido = True

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola me llamo {self.nombre}, y tengo {self.edad} años")

#fORMA EN LA QUE SE DEFINEN METODOS PRIVADOS
    def __privado(self):
        print("Soy privado")

    def acceso_protegido_padre(self):
        print(f"Puedo acceder a protegido {self._protegido}")


class PerroGuia(Perro):
    __patas = 4 # Atributo o metodo privado inicia con dos guiones bajos __

    def __init__(self, nombre, raza, edad, entrenado):
        Perro.__init__(self, nombre, edad)
        self.raza = raza
        self.entrenado = entrenado

    def validar_entrenado(self):
        if self.entrenado:
            print("Estoy entrenado")
        else:
            print("No estoy entrenado")

    def llamar_a_privado(self):
        self.__privado()

    def cuantas_patas(self):
        print(f"Tengo {self.__patas} patas")


perro = PerroGuia("Juan", "Border collie", "2 años", True)

perro.cuantas_patas()
perro.acceso_protegido_padre()

print(perro.raza)
print(perro._protegido) # No arroja error, pero no lo deberiamos usar, ya que esta protegido
# Se puede usar desde las clases que herenden al padre, pero no lo usamos desde el objeto
