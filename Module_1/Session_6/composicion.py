class Motor:

    def cilindraje(self):
        print("2000 cc")

class Llantas:

    def cuantas(self):

        print("4 llantas")


class Partes(Motor, Llantas):
    pass

class Auto:

    def __init__(self):
        self.motor = Motor()
        self.llantas = Llantas()
        self.partes = Partes()


auto = Auto()

auto.motor.cilindraje() # Motor y llantas dependen de que exista un vehiculo.

auto.llantas.cuantas()