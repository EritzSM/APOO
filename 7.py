Lista=[1,1,1,2,3,1,3,42,-1,4,2,4,2,1,4,6,4]
mayor=0
for i in range(0,len(Lista),1):
    if Lista[i]>mayor:
        mayor=Lista[i]
menor=mayor
for l in range(0,len(Lista),1):
    if Lista[l]<menor:
        menor=Lista[l]
print("El mayor es",mayor,"y el menor es",menor)