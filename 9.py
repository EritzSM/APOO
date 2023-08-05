
m=int(input("Ingrese el numero de filas"))
n=int(input("Ingrese el numero de columnas"))

matriz=[]
for i in range(0,m,1):
    fila=[]
    for l in range(0,n,1):
        fila.append(0)
    matriz.append(fila)

print(matriz)