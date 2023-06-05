"""
• Exercise 1
Write a Python program that takes two numbers as input from the user and prints
their sum.
"""

from termcolor import colored

def show_message() -> None:
    
    message = "This program adds two numbers."
    colored_message = colored(message, "white", "on_red", attrs=["bold"])
    print(colored_message)

def exercise1():
    
    while True:
        try:
            number1 = float(input("\nEnter the first number to add:\t "))
            number2 = float(input("Enter the second number to add:\t "))
            return print(f"\nThe sum of {number1} + {number2} = {number1+number2}.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    show_message()
    exercise1()

if __name__ == "__main__":
    main()
    