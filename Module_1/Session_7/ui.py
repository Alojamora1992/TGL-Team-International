import random
import pyfiglet
import scores

class Difficulty:
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class MenuOption:
    PLAY = "play"
    SCORES = "scores"
    CREDITS = "credits"
    QUIT = "quit"

def obtain_difficulty() -> str:
    difficulty = {
        "easy": Difficulty.EASY,
        "medium": Difficulty.MEDIUM,
        "hard": Difficulty.HARD
    }
    
    print("\nSELECT YOUR DIFFICULTY:\n")
    print("- EASY")
    print("- MEDIUM")
    print("- HARD")
    
    while True:
        user_input = input("\n>: ").lower()
        
        if user_input in difficulty:
            return difficulty[user_input]
        
        print("Invalid option. Try again.")
        
def show_credits() -> None:
    
    titles = [
        "Team International",
        "Top Gun Lab",
        "BY",
        "Carlos A. Posada",
        "Universidad de Antioquia"
    ]

    for title in titles:
        head = pyfiglet.figlet_format(title, font="digital", justify="center", width=100)
        print(head)
    
    show_menu()
    
def show_quit() -> None:
    T = "See you Again"
    head = pyfiglet.figlet_format(T, font="isometric1", justify="center", width=100)
    print(head) 
    exit()

def show_menu():
    menu_options = {
        "PLAY": MenuOption.PLAY,
        "SCORES": MenuOption.SCORES,
        "CREDITS": MenuOption.CREDITS,
        "QUIT": MenuOption.QUIT
    }
    
    print("\nSELECT YOUR OPTION:\n")
    for option, _ in menu_options.items():  # Usar items() para iterar sobre el diccionario correctamente
        print(f"- {option}")
    
    menu_input = input("\n>: ").lower()
    
    menu_actions = {
        "play": lambda: GuessYourNumber(obtain_difficulty()).run(),  # Llamar directamente al método run()
        "scores": lambda: scores.show_scores(),
        "credits": lambda: show_credits(),
        "quit": lambda: show_quit()
    }
    
    if menu_input in menu_actions:
        menu_actions[menu_input]()
    else:
        print("Invalid option. Try again.")
        show_menu()

class GuessYourNumber:
    def __init__(self, difficulty: str) -> None:
        self.difficulty = difficulty
        if self.difficulty == Difficulty.EASY:
            self.lower_limit = 1
            self.upper_limit = 10
        elif self.difficulty == Difficulty.MEDIUM:
            self.lower_limit = 1
            self.upper_limit = 20
        elif self.difficulty == Difficulty.HARD:
            self.lower_limit = 1
            self.upper_limit = 30
        else:
            print("Error! Try again.")

    def run(self) -> None:
        number = random.randint(self.lower_limit, self.upper_limit)
        trials = 0
        win = False
    
        while not win:
            guess = int(input("Please enter your guess: "))
            trials += 1    
            
            if guess == number:
                win = True
            elif guess < number:
                print("Too low.")
            else:
                print("Too high")
        
        print(f"\nYou win with {trials} trials.")    
        name = input("Enter your name: ")
        scores.add_score(name, trials, self.difficulty)
        show_menu()

# Llamar a la función inicial para mostrar el menú
show_menu()
