"""
Exercise 1
Write a Python class called BankAccount with methods for depositing, withdrawing,
and checking the account balance.
"""
from termcolor import colored

def show_message() -> None:
    
    message = "This program simulates a bank account by means of the concept of classes."
    colored_message = colored(message, "white", "on_red", attrs=["bold"])
    print(colored_message)

class BankAccount:
    def __init__(self,balance: float):
        self.balance = balance
        
    def depositing(self,value: float) -> None:
        self.balance += value
        
    def withdrawing(self,value: float) -> None:
        try:
            if value > self.balance:
                raise ValueError("Insufficient balance to make the withdrawal.")
            self.balance -= value
        except ValueError as error:
            print(str(error))
    
    def checking(self) -> float:
        return print(f"your current balance is {self.balance} US dollars.")


def main():
    
    show_message()
    
    #Creacion del objeto
    user_account = BankAccount(0)
    
    #depositar y chekear el cambio del balance
    user_account.depositing(500)
    user_account.checking()
    
    #Retiro exitoso y chequeo.
    user_account.withdrawing(350)
    user_account.checking()
    
    #Retiro erroneo por exceso de cantidad
    user_account.withdrawing(1000)
    
    

if __name__ == "__main__":
    main()