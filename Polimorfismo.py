class Personaje:
    def __init__(self):
        print("-- HEROE --")

    def clase(self,clase):
        print("EL HEROE es de clase: ",clase)
    
    def nivel(self,nivel):
        print("El HEROE es de nivel: ", nivel)

class UsuarioM(Personaje):
    def Mago(self,vida):
        print("VIDA: ", vida)

class UsuarioG(Personaje):
    def Guerrero(self,vida):
        print("VIDA: ", vida)

Juan = UsuarioM()
Juan.clase('MAGO')
Juan.nivel(500)
Juan.Mago(1000)

Luis = UsuarioG()
Luis.clase('GUERRERO')
Luis.nivel(500)
Luis.Guerrero(1000)