# 2 y 3 punto

import math

class Punto:
    def __init__(self,x,y):
        self.x= x
        self.y= y

    def mostrar_coordenadas(self):
        print("Las cordenadas son","(",self.x,",",self.y,")")

    def cambiar_coordenadas(self,nuevo_x,nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def distancia_coordenadas(self,otro_punto):
        distancia = math.sqrt((self.x-otro_punto.x)**2 + (self.y - otro_punto.y)**2)
        return distancia

coordenadas1 = Punto(-1,2)
coordenadas2 = Punto(4,-4)

coordenadas1.mostrar_coordenadas()
coordenadas1.cambiar_coordenadas(8,1)
coordenadas1.mostrar_coordenadas()

distancia = coordenadas1.distancia_coordenadas(coordenadas2)
print("La distancia es",distancia)
        