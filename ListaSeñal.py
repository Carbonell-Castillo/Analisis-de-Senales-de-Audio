from Señal import Señal

class nodo:
    def __init__(self, Señal=None, siguiente=None):
        self.Señal = Señal
        self.siguiente = siguiente

class lista_enlazada:
    def __init__(self):
        self.primero = None

    def insertar(self, nueva_señal):
        if self.primero is None:
            self.primero = nodo(Señal=nueva_señal)
            return
                
        actual = self.primero
        while actual:
            if actual.Señal._nombre == nueva_señal._nombre:
                print(f"La señal '{nueva_señal._nombre}' ya existe y será reemplazada.")
                actual.Señal = nueva_señal
                return
            if actual.siguiente is None:
                actual.siguiente = nodo(Señal=nueva_señal)
                return
            actual = actual.siguiente


    def recorrer(self):
        actual = self.primero
        print("Señales: \n")
        print("----------------------------------------------------------------------------")
        while actual != None:
            print("Señal: ", actual.Señal._nombre)
            actual.Señal._listaEntrada.recorrer()
            actual = actual.siguiente
            print("----------------------------------------------------------------------------")
    
    def esta_vacia(self):
        return self.primero is None