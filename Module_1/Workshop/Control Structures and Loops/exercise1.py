"""
Exercise 1
Write a Python program that prints the first 10 Fibonacci numbers using a loop.
FIBONACCI: is an infinite sequence starting from 2 numbers (1, 1) whose next number is the sum of the previous 2 numbers
"""

from termcolor import colored

def show_message() -> None:
    
    message = "\nThis program prints the first 10 Fibonacci numbers."
    colored_message = colored(message, "white", "on_red", attrs=["bold"])
    print(colored_message)
    
def fib(n):
    #Inicializo la lista con los casos base
    list = [0,1] #Convención clásica
    list = [1,1] #Convención moderna 
    
    for i in range(2,n):
        list.append(list[i-1] + list[i-2])
    return list

def main():
    
    show_message()
    print(fib(10))

if __name__ == "__main__":
    main()