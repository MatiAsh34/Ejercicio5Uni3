from Interface import *
class Coleccion(Interface):
    
    def __init__(self):
        self.__elementos = []
    
    def insertarElemento(self,elemento,posicion):
        try:
            if posicion < 0 or posicion > len(self.__elementos):
                raise PosicionInvalidaException()
            self.__elementos.insert(posicion,elemento)
            print("Elemento insertado!")
        except:
            print("La posicion de insercion no es valida!")
    
    def agregarElemento(self, elemento):
        self.__elementos.append(elemento)
        print("Elemento insertado!")
    
    def mostrarElemento(self,posicion):
        try:
            if posicion < 0 or posicion >= len(self.__elementos):
                raise PosicionInvalidaException()
            print("Elemento: ",self.__elementos[posicion])
        except:
            print("No hay elemento en esa posicion!")
