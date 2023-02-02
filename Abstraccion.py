class Auto(object):
    def setMarca(self,marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

AUTOMOVIL = Auto()
AUTOMOVIL.setMarca("TOYOTA")
print(AUTOMOVIL.getMarca())