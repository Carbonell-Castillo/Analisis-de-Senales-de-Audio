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
    print("Recorrer: \n")
    print("----------------------------------------------------------------------------")
    while actual != None:
      print("Tiempo: ", actual.Dato._tiempo, " Amplitud: ", actual.Dato._Amplitud)
      actual = actual.siguiente
    print("----------------------------------------------------------------------------")


  

    
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