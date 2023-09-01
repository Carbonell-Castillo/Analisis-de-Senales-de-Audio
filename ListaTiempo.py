from Tiempo import Tiempo
        

class nodo:
  def __init__(self, Tiempo=None, siguiente=None):
    self.Tiempo = Tiempo
    self.siguiente = siguiente

class lista_enlazada:
    def __init__(self):
        self.primero = None
    
    def insertar(self, Tiempo):
        if self.primero is None:
            self.primero = nodo(Tiempo=Tiempo)
            return
        
        # Verificar si el tiempo ya existe en la lista
        tiempo_existente = self.buscar_tiempo(Tiempo._tiempo)
        if not tiempo_existente:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo(Tiempo=Tiempo)
    
    def buscar_tiempo(self, tiempo):
        actual = self.primero
        while actual:
            if actual.Tiempo._tiempo == tiempo:
                return True  # El tiempo ya existe en la lista
            actual = actual.siguiente
        return False  # El tiempo no existe en la lista
    
    def recorrer(self):
        actual = self.primero
        while actual:
            print(actual.Tiempo._tiempo)
            actual = actual.siguiente
    
    def limpiar(self):
        self.primero = None