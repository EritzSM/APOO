class Carta:
    PINTAS = ["Treboles","Diamantes","Corazones","Picas"]
    
    def __init__(self,valor,pintas):
        self.valor = valor
        self.pintas = pintas

Carta1 = Carta("10","Treboles")  
Carta2 = Carta("9","Diamantes")

print(Carta1.valor,"de",Carta1.pintas)
print(Carta2.valor,"de",Carta2.pintas)


        