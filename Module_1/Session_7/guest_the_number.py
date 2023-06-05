"""La idea es crear un juego que tenga un menu, dentro de este menu se tendran las opciones de jugar, puntuacion y salir.

1. Jugar
2. Puntuaciones
3. Creditos
4. Salir

si el usuario elije jugar, debera escoger la dificulta, que sera facil , medio y dificil. Dependiendo de la dificultad, se calculara el numero a hallar (Aleatoriamente) y si el numero esta por debajo del # a adivinar que diga que es too low y viceversa si es mayor."""

import json
import random
import pyfiglet
import os
from tabulate import tabulate
from enum import Enum
from datetime import datetime

# Encabezado inicial del juego.
T = "Guess Your Number"
head = pyfiglet.figlet_format(T, font="banner3", justify="center", width=110)
print(head)


class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

    def __str__(self):
        return self.value


class MenuOption(Enum):
    PLAY = "play"
    SCORES = "scores"
    CREDITS = "credits"
    QUIT = "quit"

    def __str__(self):
        return self.value


class GuessYourNumber:
    def __init__(self, difficulty: Difficulty) -> None:
        self.difficulty = difficulty
        if self.difficulty == Difficulty.EASY:
            self.number = random.randint(1, 10)
        elif self.difficulty == Difficulty.MEDIUM:
            self.number = random.randint(1, 20)
        elif self.difficulty == Difficulty.HARD:
            self.number = random.randint(1, 30)
        else:
            print("Error! Try again.")

    def run(self) -> None:
        trials = 0
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
        name = input("Enter your name: ")
        score = trials
        generate_scores_txt(name, score, self.difficulty)


def obtain_difficulty() -> Difficulty:
    difficulty = {
        "easy": Difficulty.EASY,
        "medium": Difficulty.MEDIUM,
        "hard": Difficulty.HARD
    }

    print("\nSELECT YOUR DIFFICULTY:")
    print("1. EASY")
    print("2. MEDIUM")
    print("3. HARD")

    user_input = input(">: ").lower()

    if user_input in difficulty:
        return difficulty[user_input]
    else:
        print("Invalid option. Try again.")
        return obtain_difficulty()


def write_scores_to_file(scores: list) -> None:
    with open("scores.json", "w") as file:
        json.dump(scores, file, indent=4)


def generate_scores_txt(name: str, trials: int, difficulty: Difficulty) -> None:
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists("scores.json"):
        with open("scores.json", "r") as file:
            scores = json.load(file)
    else:
        scores = []

    scores.append({
        "username": name,
        "difficulty": str(difficulty),
        "trials": trials,
        "fecha": date_time
    })

    write_scores_to_file(scores)

    print("Score:")
    print("-------")
    print("Name\t\t\tTrials\t\t\tDate\t\t\tDifficulty")
    print("-" * 90)
    print(f"{name}\t\t\t{trials}\t\t\t{date_time}\t{str(difficulty)}")


def select_menu_option() -> MenuOption:
    menu = {
        "play": MenuOption.PLAY,
        "scores": MenuOption.SCORES,
        "credits": MenuOption.CREDITS,
        "quit": MenuOption.QUIT
    }

    print("\nSELECT YOUR OPTION:")
    print("1. PLAY")
    print("2. SCORES")
    print("3. CREDITS")
    print("4. QUIT")

    menu_input = input(">: ").lower()

    if menu_input in menu:
        return menu[menu_input]
    else:
        print("Invalid option. Try again.")
        return select_menu_option()


def show_credits() -> None:
    T1 = "Team International"
    T2 = "Top Gun Lab"
    T3 = "BY"
    T4 = "Carlos A. Posada"
    T5 = "Universidad de Antioquia"
    head1 = pyfiglet.figlet_format(T1, font="digital", justify="center", width=100)
    head2 = pyfiglet.figlet_format(T2, font="bulbhead", justify="center", width=100)
    head3 = pyfiglet.figlet_format(T3, font="digital", justify="center", width=100)
    head4 = pyfiglet.figlet_format(T4, font="digital", justify="center", width=100)
    head5 = pyfiglet.figlet_format(T5, font="digital", justify="center", width=100)
    print(head1)
    print(head2)
    print(head3)
    print(head4)
    print(head5)
    main()


def show_quit() -> None:
    T = "See you Again"
    head = pyfiglet.figlet_format(T, font="isometric1", justify="center", width=100)
    print(head)


def main() -> None:
    option_menu = select_menu_option()

    if option_menu == MenuOption.PLAY:
        level = obtain_difficulty()
        game = GuessYourNumber(level)
        game.run()
    elif option_menu == MenuOption.SCORES:
        if os.path.exists("scores.json"):
            with open("scores.json", "r") as file:
                scores = json.load(file)
                print_scores(scores)
        else:
            print("No scores found.")
    elif option_menu == MenuOption.CREDITS:
        show_credits()
    elif option_menu == MenuOption.QUIT:
        show_quit()
    else:
        print("Invalid option. Try again.")

def print_scores(scores):
    sorted_scores = sorted(scores, key=lambda x: x['trials'])
    
    print("Scores:")
    print("-------")
    print("Name\t\t\tTrials\t\t\tDate\t\t\tDifficulty")
    print("-" * 90)
    for score in sorted_scores:
        print(f"{score['username']}\t\t\t{score['trials']}\t\t\t{score['fecha']}\t{score['difficulty']}")


if __name__ == '__main__':
    main()

