from Coleccion import *
   
if __name__ == "__main__":
    UnaColeccion=Coleccion()

    opcion=None

    while opcion!='0':
        print ("\n1: Insertar elemento en una posición")
        print ("2: Insertar elemento al final")
        print ("3: Mostrar un elemento")
        print ("0: Salir")
    
        opcion=input("\nIngrese una opción: ")

        if opcion == '1':
            elemento = int(input("\nIngrese un elemento: "))
            posicion = int(input("Ingrese una posicion: "))
            UnaColeccion.insertarElemento(elemento,posicion)

        if opcion == '2':
            elemento = int(input("\nIngrese un elemento: "))
            UnaColeccion.agregarElemento(elemento)

        if opcion == '3':
            posicion = int(input("\nIngrese una posicion: "))
            UnaColeccion.mostrarElemento(posicion)

        if opcion == '0':
            print("\nSaliendo...")