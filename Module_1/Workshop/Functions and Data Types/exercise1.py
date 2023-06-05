"""
Exercise 1
Write a Python function called find_maximum that takes a list of numbers as input
and returns the maximum number from the list.
"""

from termcolor import colored

def show_message() -> None:
    
    message = "This program returns the maximum number of the list."
    colored_message = colored(message, "white", "on_red", attrs=["bold"])
    print(colored_message)

def find_maximum(list: list) -> float:
    max = 0
    
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return print(f"The max number on the list {list} is: {max}")


def request_data() -> list:
    while True:
        list_numbers = input("\nEnter a list of number separated for spaces: ")
        list_numbers = list_numbers.split()
        try:
            list_numbers = [float(num) for num in list_numbers]
            return list_numbers
        except ValueError:
            print("Error, please enter only numbers. Try again.")
               
def main():
    
    show_message()
    list = request_data()
    find_maximum(list)


if __name__ == "__main__":
    main()