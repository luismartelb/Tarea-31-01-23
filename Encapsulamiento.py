class Encapsulamiento:
    variable_1= 'a'#accesible
    _variable_2= 'b'#Protegido
    __variable_3= 'c'#privado

    def __init__(self):
        print(self.variable_1)
        print(self._variable_2)
        print(self.__variable_3)

object_Capsula = Encapsulamiento
print(object_Capsula.variable_1)
print(object_Capsula._variable_2)
print(object_Capsula.__variable_3)