"""
Exercise 2
Create a Python decorator called timer that measures the time taken to execute a function. Use this decorator on a function that sorts a list of random numbers and prints the sorted list

Python decorator: Sirve para agregar mas funcionalidades a una funcion, sin modificar su estructura.
"""

import random
import time
from functools import wraps
from termcolor import colored

def show_message() -> None:
    
    message = "This program adds the execution time of a function that organizes the elements of a list, without modifying its structure."
    colored_message = colored(message, "white", "on_red", attrs=["bold"])
    print(colored_message)



def timer(func):
    @wraps(func)
    def wrapper(lista):
        start_time = time.perf_counter()
        result = func(lista)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"The function '{func.__name__}' delay {execution_time:.6f} sec. to execute.")
        return result
    return wrapper

@timer
def sorted_list(lista):
    return sorted(lista)


def main():

    show_message()
    number_list = [random.randint(1, 90) for _ in range(40)]
    sort_list = sorted_list(number_list)
    print("Original list:\t", number_list)
    print("Sorted list:\t", sort_list)

if __name__ == "__main__":
    main()