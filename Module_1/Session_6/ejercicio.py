"""Debes crear una clase auto con atributos como marca, modelo, anio, velocidad y metodos como acelerar  el cual va a aumentar el valor de la velocidad, frenar que va  a poner la velocidad en 0. Luego, crear una clase autoelectrico que herede de auto y tenga un atributo adiccional, autonomia, porcentaje de bateria y un metodo adicional cargar bateria, el cual va aumentar el valor de la bateria de 10 en 10 hasta llegar a 100, cuando llegue a 100 mostrara carga finalizada."""

class Auto:
    def __init__(self,marca: str, modelo: int, velocidad: float):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
    
    def acelerar(self, acelerar:float):
        self.velocidad += acelerar
        print(f"Velocidad: {self.velocidad}")
    
    def frenar(self):
        self.velocidad = 0
        print(f"velocidad: {self.velocidad}")
        
class AutoElectrico(Auto):
    def __init__(self,marca: str, modelo: int, velocidad: float, autonomia: str, porcentaje_bateria: float):
        super().__init__(marca,modelo,velocidad)
        self.autonomia = autonomia
        self.porcentaje_bateria = porcentaje_bateria
    
    def cargar_Bateria(self):
        while self.porcentaje_bateria < 100:
            
            if self.porcentaje_bateria + 10 <= 100:
                self.porcentaje_bateria += 10 
                print(f"porcentaje de bateria: {self.porcentaje_bateria} %, cargando...")
            else:
                self.porcentaje_bateria = 100
                print(f"porcentaje de bateria: {self.porcentaje_bateria} %, carga finalizada.")
                

auto_electrico = AutoElectrico("Toyota",1985,35.6,"si", 46.2)

print(f"V_inicial: {auto_electrico.velocidad}")
auto_electrico.acelerar(30)
auto_electrico.frenar()

print(f"porcentaje de bateria: {auto_electrico.porcentaje_bateria} %")
auto_electrico.cargar_Bateria()
