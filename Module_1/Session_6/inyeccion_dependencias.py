
class Servicio:
    def hacer_algo(self):
        print("Este servicio hace algo")


class Cliente:

    def __init__(self, servicio: Servicio):
        self.servicio = servicio

    def user_servicio(self):
        self.servicio.hacer_algo()
        print("Este servicio fue usado")



servicio = Servicio()

cliente_1 = Cliente(servicio)
cliente_1.user_servicio()


cliente_2 = Cliente(servicio)
cliente_2.user_servicio()