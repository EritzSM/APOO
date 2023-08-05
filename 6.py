Lista = []
numero=int(input("Ingrese un numero "))
Lista.append(numero)
numero=int(input("Ingrese un numero "))
Lista.append(numero)  
while True:
    x=int(input("Desea seguir agregando numeros?  Si=1  No=2")) 
    if x==2:
        break
    else:
        numero=int(input("Ingrese un numero "))
        Lista.append(numero)  
       
Suma=0
for i in range(0,len(Lista),1):
    Suma=Suma+Lista[i]
print("Su suma es",Suma)