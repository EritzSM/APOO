import math

class Circulo:
    def __init__(self, centro_x, centro_y, radio):
        self.centro_x = 0
        self.centro_y = 0
        self.radio = 5
    
    def calcular_area(self):
        return math.pi * self.radio**2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
    def punto_pertenece(self, x, y):
        distancia_centro = math.sqrt((x - self.centro_x)**2 + (y - self.centro_y)**2)
        return distancia_centro <= self.radio
    
circulo = Circulo(None,None,None)

area = circulo.calcular_area()
perimetro = circulo.calcular_perimetro()

print("Área del círculo es:",area)
print("Perímetro del círculo:",perimetro)


x_punto = 2
y_punto = 2
if circulo.punto_pertenece(x_punto, y_punto):
    print(f"El punto ({x_punto}, {y_punto}) pertenece al círculo.")
else:
    print(f"El punto ({x_punto}, {y_punto}) no pertenece al círculo.")
