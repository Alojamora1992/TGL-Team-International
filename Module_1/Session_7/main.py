import pyfiglet
import ui

T = "Guess Your Number"
head = pyfiglet.figlet_format(T, font="banner3", justify="center", width=110)
print("\n\n")
print(head)

if __name__ == '__main__':
    ui.show_menu()

