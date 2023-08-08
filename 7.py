
class CuentaBancaria:
    def __init__(self,Numero_cuenta,Propietarios,Balance):
        self.Numero_cuenta = Numero_cuenta
        self.Propietarios = Propietarios
        self.Balance = Balance

    def depositar(self,Monto):
        if Monto<0:
            print("No se pueden introducir numeros negativos")
        else:
            self.Balance+=Monto
            print("Su balance es",self.Balance)
        

    def retirar(self,Monto):
        if 0 < Monto <= Balance:
            self.Balance-=Monto
            print("Su balance es",self.Balance)
        else:
            print("No tiene suficiente saldo")
            

    def aplicar_cuota(self):
        cuota = self.Balance * 0.02
        self.Balance -= cuota
        print("Su cuota de manejo es",cuota,"y su balance actual es",self.Balance)
    
    def mostrar_detalles(self):
        print("Numero de cuenta:",self.Numero_cuenta )
        print("Propietario:",self.Propietarios)
        print("Balance:",self.Balance)
    
        while True:
            print("Si desea depositar marque 1 ")
            print("Si desea retirar marque 2 ")
            print("Si desea aplicar marque 3 ")
            print("Si desea mostrar detalles marque 4 ")
            x= int(input("¿Que desea hacer?"))

            if x == 1:
                Monto = int(input("Ingrese el monto que desea depositar "))
                self.depositar(Monto)
            if x == 2:
                Monto = int(input("Ingrese el monto que desea retirar "))
                self.retirar(Monto)
            if x == 3:
                self.aplicar_cuota()
            if x == 4:
                self.mostrar_detalles()
            if x == 5:
                break

Numero_cuenta=(int(input("Ingresa el numero de cuenta ")))
Propietarios=(str(input("Ingresa el nombre del propietarios ")))
Balance=(int(input("Ingresa el balance ")))
         
Cuenta_1 = CuentaBancaria(Numero_cuenta,Propietarios,Balance)

Cuenta_1.mostrar_detalles()

    