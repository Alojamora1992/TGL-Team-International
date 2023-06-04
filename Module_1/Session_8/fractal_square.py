import turtle
import random

#Variables globales
WIDTH = 600
HEIGTH = 600
color_palette = ["red", "green", "blue", "yellow", "orange"]

#Configuracion de la instancia turtle
def config_turtle(width: int, height:int) -> None:
    
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.screensize(width, height)
    screen.title("Sierpinsky Carpet")
    turtle.speed(0)

#funcion que dibuja cada cuadrado    
def draw_square(x:int, y:int, length: int, color: str) -> None:
    
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()
    
    turtle.color(color)
    turtle.begin_fill()
    
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)
        
    turtle.end_fill()
   
#Funcion que dibuja el fractal utilziando recursividad.
def draw_carpet(offset_x, offset_y, length, level, color) -> None:
    #Dibujo del cuadro principal donde se hara el fractal.
    draw_square(offset_x, offset_y, length, color = "black")
    
    #asignacion del color dependiendo del nivel de profundidad.
    color_index = level - 1
        
    if color_index < len(color_palette):
        color = color_palette[color_index]
    else:
        color = random.choice(color_palette)
    
    #1er caso base
    if level == 0:
        return
    #2do caso base
    if level == 1:
        
        sublength = length // 3
        draw_square(offset_x + sublength, offset_y - sublength, sublength, color)
        
    #caso general utilizando recursividad.
    if level > 1:
        sublength = length // 3
         
        for i in range(3):
            for j in range(3):
                #Caso base de la recursividad:
                if i == 1 and j == 1:
                    draw_square(offset_x + sublength, offset_y - sublength, sublength, color)
                else:  
                    draw_carpet(offset_x + i*sublength, offset_y - j*sublength, sublength, level-1, color)
 
#Solicitud de datos al usuario.               
def request_data():
    while True:
        try:
            length = int(input("Ingrese la longitud del fractal: "))
            level = int(input("Ingrese el nivel de profundidad: "))
            return length, level
        except ValueError:
            print("Error: Debes ingresar un número entero válido. Intenta nuevamente.")

#Menu principal.  
def main():
    #Configuracion de turtle
    config_turtle(WIDTH,HEIGTH)
    
    #Solcitar datos al ususario:
    length, level = request_data()
    
    #Dibujar fractal de sierpinsky cuadrado
    color = random.choice(color_palette)
    draw_carpet(-length/2,length/2,length, level, color)
    
    turtle.done()
    

if __name__ == '__main__':
    main()