from dataclasses import dataclass

@dataclass
class Elemento:
    nombre:str
    
    def __eq__(self, otro:str) -> bool:
        self.otro:str = otro
        return self.nombre == self.otro

class Conjunto:
    contador = 0  

    def __init__(self, nombre):
        self.elementos = [] 
        self.nombre = nombre 
        self.__id = Conjunto.contador 
        Conjunto.contador += 1 

    @property
    def id(self):
        return self.__id  

    def contiene(self, elemento):
        return any(e == elemento for e in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNION {otro_conjunto.nombre}")
        nuevo_conjunto.elementos.extend(self.elementos)
        for elemento in otro_conjunto.elementos:
            if not nuevo_conjunto.contiene(elemento):
                nuevo_conjunto.elementos.append(elemento)
        return nuevo_conjunto

    def __add__(self, otro_conjunto):
        return self.unir(otro_conjunto)

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_interseccion = [elemento for elemento in conjunto1.elementos if conjunto2.contiene(elemento)]
        nombre_interseccion = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        nuevo_conjunto = Conjunto(nombre_interseccion)
        nuevo_conjunto.elementos = elementos_interseccion
        return nuevo_conjunto

    def __str__(self):
        elementos_str = ", ".join([elemento.nombre for elemento in self.elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})"

