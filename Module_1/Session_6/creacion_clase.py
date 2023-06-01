class Perro:
    def __init__(self,name: str, age: int):
        self.name = name
        self.age = age
    
    def saludar(self):
        print(f"Hi my name is {self.name} and i'm {self.age} years old.")
        self.despedida()
        
    def despedida(self):
        print(f"Adios.")
    
    #Metodos magicos    
    def __str__(self):
        return "I'm a dog"
        
perro  = Perro("Nemesis", 2)

perro.saludar()