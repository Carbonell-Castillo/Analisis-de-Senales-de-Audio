from Dato import Dato
import os
class nodo:
  def __init__(self, Dato=None, siguiente=None):
    self.Dato = Dato
    self.siguiente = siguiente

class lista_enlazada:
  def __init__(self):
    self.primero = None
  
  def insertar(self, Dato):
    if self.primero is None:
      self.primero = nodo(Dato=Dato)
      return
    actual = self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo(Dato=Dato)

  def recorrer(self):
    actual = self.primero
    print("Datos: \n")
    print("----------------------------------------------------------------------------")
    while actual != None:
      print("Tiempo: ", actual.Dato._tiempo, " Amplitud: ", actual.Dato._amplitud, "Dato: ", actual.Dato._dato)
      actual = actual.siguiente
    print("----------------------------------------------------------------------------")

  def recorrer2(self):
    actual = self.primero
    print("Recorrer2: \n")
    while actual != None:      
      actual = actual.siguiente
      return actual.Dato
    
  def recorrer3(self):
    actual = self.primero
    segundo = self.primero
    print("Tiempo: ", actual.Dato._tiempo)
    while actual != None:

        segundo = segundo.siguiente
        if segundo != None:
            if actual.Dato._tiempo == segundo.Dato._tiempo:
                
                
                print(actual.Dato._dato, end="")
                if actual.siguiente:  # Solo imprime la flecha si hay un nodo siguiente
                    print(" -> ", end="")
                actual = actual.siguiente
            else:
                print(actual.Dato._dato, end="")
                print("")
                actual= actual.siguiente            
                print("Tiempo: ", actual.Dato._tiempo)
        else:
            print(actual.Dato._dato, end="")
            actual = actual.siguiente
    print("")

  def contar_elementos(self):
        temp = self.primero
        count = 0
        while temp:
            count += 1
            temp = temp.siguiente
        return count

  def buscar_tiempo(self, tiempo):
    actual = self.primero

    while actual:
        if actual.Dato._tiempo == tiempo :
            print("Tiempo Econtrado: ", actual.Dato._tiempo, "Amplitud: ", actual.Dato._amplitud)
            return actual.Dato._amplitud            
        actual = actual.siguiente

    return False
  

    
  def esta_vacia(self):
    return self.primero is None
#   def eliminar(self, usuario):
#     actual = self.primero
#     anterior= None

#     while actual and actual.nota.usuario != usuario:
#       anterior = actual
#       actual = actual.siguiente

#     if anterior is None:
#       self.primero = actual.siguiente
#       actual.siguiente = None
#     elif actual:
#       anterior.siguiente = actual.siguiente
#       actual.siguiente = None

#   def buscar(self, usuario):
#     actual = self.primero
#     anterior= None

#     while actual and actual.nota.usuario != usuario:
#       anterior = actual
#       actual = actual.siguiente

#     if anterior is None:
#       self.primero = actual.siguiente
#       print("Usuario: ", actual.nota.usuario, "| Titulo: ", actual.nota.titulo, "| Libreta: ", actual.nota.libreta, "| Contenido: ", actual.nota.contenido, "| Fecha creacion:", actual.nota.fecha_creacion, "| Fecha modificacion: ", actual.nota.fecha_modificacion, "| Tipo acceso: ", actual.nota.tipo_acceso)
#     elif actual:
#       anterior.siguiente = actual.siguiente
#       print("Usuario: ", actual.nota.usuario, "| Titulo: ", actual.nota.titulo, "| Libreta: ", actual.nota.libreta, "| Contenido: ", actual.nota.contenido, "| Fecha creacion:", actual.nota.fecha_creacion, "| Fecha modificacion: ", actual.nota.fecha_modificacion, "| Tipo acceso: ", actual.nota.tipo_acceso)