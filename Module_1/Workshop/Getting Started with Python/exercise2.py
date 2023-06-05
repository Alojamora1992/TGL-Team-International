"""
Exercise 2
Create a Python program that converts a temperature from Fahrenheit to Celsius.
The user should enter the temperature in Fahrenheit, and the program should print
the equivalent temperature in Celsius.
"""

from termcolor import colored


def show_message() -> None:
    
    message = "This program converts a temperature from degrees Fahrenheit to degrees Celsius."
    colored_message = colored(message, "white", "on_red", attrs=["bold"])
    print(colored_message) 

def exercise2():
    
    while True:
        
        try:
            farenheit = float(input("\nEnter the temperature in degree Farenheit: "))
            return print(f"Temperature in degree Celsius: {round((farenheit-32)*5/9,2)} °C")
        
        except ValueError:
            print("Error, please enter a valid number.")

def main():
    
    show_message()
    exercise2()

if __name__ == "__main__":
    main()