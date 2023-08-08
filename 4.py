class Rectangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def calcular_area_perimetro(punto1, punto2):
    base = abs(punto1.x - punto2.x)
    altura = abs(punto1.y - punto2.y)
    
    if base == altura:
        print("Es un rectangulo cuadrado")
    else:
        print("No es un rectangulo cuadrado")

    area = base * altura
    perimetro = 2 * (base + altura)
    
    return area, perimetro


punto1 = Rectangulo(2, 3)
punto2 = Rectangulo(7, 8)

area, perimetro = calcular_area_perimetro(punto1, punto2)



print("Área del rectángulo es:",area)
print("Perímetro del rectángulo:",perimetro)



 
        