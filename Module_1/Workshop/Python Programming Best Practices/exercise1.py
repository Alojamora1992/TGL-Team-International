"""
Exercise 1
Write a Python function called is_palindrome that checks if a given word is a palindrome. The function should have proper error handling and be tested withunittest.
"""

from termcolor import colored

def show_message() -> None:
    
    message = "This program checks if a word is a palindrome or not."
    colored_message = colored(message, "white", "on_red", attrs=["bold"])
    print(colored_message)

def reverse_string(string: str) -> str:

    list_reverse = []
    for i in range(len(string) - 1, -1, -1):
        list_reverse.append(string[i])
    return ''.join(list_reverse)
 
def request_data() -> list:
    
    while True:
        try:
            word = input("Please, enter a word: ")
            if not word.isalpha():
                raise ValueError("Invalid input. Please enter only words.")
            return word
        except ValueError as error:
            print(str(error))

def is_palindrome(word: str) -> bool:
    
    return word == reverse_string(word)
    # if word == reverse_string(word):
    #     return print(f"The word {word} is palindrome: {True}")
    # else:
    #     return print(f"The word {word} is palindrome: {False}")
    
def main():
    
    show_message()
    word = request_data()
    is_palindrome(word)

if __name__ == "__main__":
    main()