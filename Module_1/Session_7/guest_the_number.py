"""La idea es crear un juego que tenga un menu, dentro de este menu se tendran las opciones de jugar, puntuacion y salir.

1. Jugar
2. Puntuaciones
3. Salir

si el usuario elije jugar, debera escoger la dificulta, que sera facil , medio y dificil. Dependiendo de la dificultad, se calculara el numero a hallar (Aleatoriamente) y si el numero esta por debajo del # a adivinar que diga que es too low y viceversa si es mayor."""

import random
import pyfiglet
from enum import Enum


class Dificultad(Enum):
    FACIL = "facil"
    MEDIO = "medio"
    DIFICIL = "dificil"

class Menu(Enum):
    JUGAR = "jugar"
    SCORES = "scores"
    CREDITS = " credits"
    OUT = "out"

class GuestYourNumer:
    def __init__(self, dificultad: Dificultad) -> None:
        
        #Construyendo dificultad
        if dificultad == Dificultad.FACIL:
            self.number = random.randint(1,10)
        elif dificultad == Dificultad.MEDIO:
            self.number = random.randint(1,20)
        elif dificultad == Dificultad.DIFICIL:
            self.number = random.randint(1,30)
        else:
            print("Error! try again.")

    #Metodo para correr el juego.
    def run(self):

        trials = 0
        #Flag variable
        win = False
    
        while not win:
            guess = int(input("Please enter your guess: "))
            trials += 1    
            
            if guess == self.number:
                win = True
            elif guess < self.number:
                print("Too low.")
            else:
                print("Too high")
        
        print(f"You win with {trials} trials.")

def obtain_difficulty():
    
    dificultad = {
        "facil": Dificultad.FACIL,
        "medio": Dificultad.MEDIO,
        "dificil": Dificultad.DIFICIL
    }
    
    print("")
    print("SELECT YOUR DIFFICULTY:")
    print("")
    print("1. FACIL")
    print("2. MEDIO")
    print("3. DIFICIL")
    print("")
    user_input = (input(">: ")).lower() # Nos aseguramos de poner en minuscula la entrada del usuario.
    
    if user_input in dificultad:
        return dificultad[user_input]
    else:
        print("Opción inválida. Intenta nuevamente.")
        return obtain_difficulty()
    
def generate_txt():
    pass

def show_menu():
    
    T = "Guest Your Number "
    head = pyfiglet.figlet_format(T, font="banner3", justify = "center", width = 110)
    print(head)
    
    menu = {
        "JUGAR": Menu.JUGAR,
        "SCORES": Menu.SCORES,
        "CREDITS": Menu.CREDITS,
        "OUT": Menu.OUT
    }
    
    print("")
    print("SELECT YOUR OPTION:")
    print("")
    print("1. JUGAR")
    print("2. SCORES")
    print("3. CREDITS")
    print("4. OUT.")
    print("")
    menu_input = (input(">: ")).lower()
    
    if menu_input in menu:
        return menu[menu_input]
    else:
        print("Opción inválida. Intenta nuevamente.")
        return show_menu()
    

#Funcion principal
def main():
    show_menu()
    level = obtain_difficulty()
    game = GuestYourNumer(level)
    game.run()

if __name__ == '__main__':
    main()