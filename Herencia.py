class Auto:
    def __init__(self,color):
        self.color = color
        print("El auto es de color: ",color)

    def clase(self,marca):
        self.marca = marca
        print("La marca es: ", marca)

class Vehiculo(Auto):
    def serie(self,modelo):
        print("EL modelo es: ",modelo)

taxi = Vehiculo('Rojo')

taxi.clase('AUDI')
taxi.serie('A5')
