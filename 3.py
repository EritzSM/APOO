import random

Cuantos = int(input("De que tamaño quiere la lista "))
Lista = []
for i in range(0,Cuantos,1):
    Lista.append(random.randint(1,100)) 

print(Lista)