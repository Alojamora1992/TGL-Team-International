"""
Exercise 2
Create a Python program that checks if a given number is prime or not. The user
should input a number, and the program should print whether it is prime or not.
"""
from termcolor import colored
import math

def show_message() -> None:
    
    message = "\nThis program checks whether a number entered by the user is prime or not."
    colored_message = colored(message, "white", "on_red", attrs=["bold"])
    print(colored_message)

def is_prime(number: int) -> str:
    
    if number <= 1:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    
    return True

def request_data() -> int:
    while True:
        try:
            number = int(input("Enter the number to calculate: "))
            return number
        except ValueError:
            print("Error, invalid number.")
    
def main():
    
    show_message()
    number = request_data()   
    print(f"The number {number} is prime: {is_prime(number)}")

if __name__ == "__main__":
    main()
