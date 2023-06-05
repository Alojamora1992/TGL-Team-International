"""
Exercise 2
Create a Python program that reads a text file and counts the occurrences of each
word using a dictionary. The program should print the words and their counts.

Steps:
1. read file
2. counts occurrences, create diccionary key: word, value: count ocurrences
3. show 2
"""

from termcolor import colored

def show_message() -> None:
    
    message = "This program reads a text file .txt file and displays the number of each of the words."
    colored_message = colored(message, "white", "on_red", attrs=["bold"])
    print(colored_message)

def read_file(text: str) -> list:
    # Abre el archivo en modo lectura utilizando with open
    with open(text, "r") as file:
        # Lee todo el contenido del archivo
        contenido = file.read()

    # Divide el contenido en palabras
    words = contenido.split()
    return words

def show_diccionary(words_list: list):
    
    diccionario  = {}
    for word in words_list:
        diccionario[word] = words_list.count(word)
        
    for word, count in diccionario.items():
        print(f"Palabra: {word.ljust(20)}\t\tCantidad: {count}")

def main():
    show_message()
    
    #test1
    list1 = read_file("text1.txt")
    show_diccionary(list1)
    print("\n")
    #test2
    list2 = read_file("text2.txt")
    show_diccionary(list2)
    
    

if __name__ == "__main__":
    main()