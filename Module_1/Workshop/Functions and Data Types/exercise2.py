"""
Exercise 2
Create a Python function called reverse_string that takes a string as input and returns
the reversed string.
"""

from termcolor import colored

def show_message() -> None:
    
    message = "This program returns one entered by the user backwards."
    colored_message = colored(message, "white", "on_red", attrs=["bold"])
    print(colored_message)

def reverse_string(string: str) -> str:

    # Forma recursividad by Luis P.
    # if string: 
    #     return string[-1] + reverse_string(string[:-1])   
    # else:
    #     #caso base
    #     return ""
    
    #Mi forma
    list_reverse = []
    for i in range(len(string) - 1, -1, -1):
        list_reverse.append(string[i])
    return ''.join(list_reverse)

def request_data() -> list:
    while True:
        try:
            word = input("\nEnter some word: ")
            return word
        except ValueError:
            print("Error, please enter only strings. Try again.")

def main():
    
    show_message()
    word = request_data()
    print("The word in reverse is:", reverse_string(word))
    

if __name__ == "__main__":
    main()