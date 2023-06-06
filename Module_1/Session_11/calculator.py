"""
Ej de expresiones:
2+3-1

TOKENS:
numbers = 1,2,3,4,5,6,7,8,9,0
minus = -
plus = +
multiplication = *
division = /
left_parenthesis = (
right_parenthesis = )
equal = =

ej continuando la expresion anterior:
Token(NUMBERS, 2) Token(PLUS, +) Token(NUMBERS, 3) Token(MINUS, -) Token(NUMBERS, 1)
"""

from enum import Enum

#Variables globales
ALLOWED_CHARACTERS = set("0123456789+-*/()")


#Definicion de la clase tokens
class Tokens(Enum):
    NUMBERS = "NUMBERS"
    MINUS = "MINUS"
    PLUS = "PLUS"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    LEFT_PARENTHESIS = "LEFT_PARENTHESIS"
    RIGHT_PARENTHESIS = "RIGHT_PARENTHESIS"
    EQUAL = "EQUAL"
    NULL = "NULL"

#definicion clase token
class Token:
    def __init__(self, token_type: Tokens, value: str):
        self.token_type = token_type
        self.value = value
    
    def __repr__(self):
        return f"Token({self.token_type.value}, {self.value})"

class Lexer:
        
    def reset(self, expression: str) -> None:
        self.expression = expression
        self.current_char_position = 0
        
    def get_next_token(self) -> Token:
        while self.current_char_position < len(self.expression):
            if self.expression[self.current_char_position].isdigit():
                token = Token(Tokens.NUMBERS, int(self.expression[self.current_char_position]))
                self.current_char_position += 1
                return token
            elif self.expression[self.current_char_position] == "+":
                token = Token(Tokens.PLUS, "+")
                self.current_char_position += 1
                return token
            elif self.expression[self.current_char_position] == "-":
                token = Token(Tokens.MINUS, "-")
                self.current_char_position += 1
                return token
            
        return Token(Tokens.NULL, None)


def test():
    token = Token(Tokens.NUMBERS, "1")
    print(token)

def main():
    
    lexer = Lexer()
    string = ""
    
    while string.lower() !="x":
        
        try: 
            string = input("Enter a mathematical expression: ")
            
            #Validacion de caracteres
            lexer.reset(string)
            current_token = lexer.get_next_token()
            while current_token.token_type != Tokens.NULL:
                print(current_token)
                current_token = lexer.get_next_token()
            
            if not set(string).intersection(ALLOWED_CHARACTERS):
                raise ValueError("Invalid characters in expression.")
        except ValueError as error:
            print(str(error))
    
    print("\nThanks for using our calculator. Goodbye!")
    
    
if __name__ == "__main__":
    main()