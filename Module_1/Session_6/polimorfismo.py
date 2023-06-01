#herencia del padre, pero con valores y acciones diferentes.

class Ave:
    def volar(self):
        pass #El pass quiere decir continue o siga al estar vacia


class Aguila(Ave):

    def volar(self):
        print("Puedo volar")


class Pinguino(Ave):

    def volar(self):
        print("No puedo volar")

aguila = Aguila()

aguila.volar()

pinguino = Pinguino()

pinguino.volar()
