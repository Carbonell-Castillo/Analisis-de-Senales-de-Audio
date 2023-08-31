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
 
  def generarMatrizFrecuencia(self):
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

  def gene2(self):
    actual = self.primero
    print("Tiempo:", actual.Dato._tiempo)
    tiempoAnterior = actual.Dato._tiempo
    print("Tiempo:", actual.Dato._tiempo)
    primerDatoMismoTiempo = None
    grupoValido=False
    count=1
    while actual is not None:
        segundo = self.primero
        while segundo is not None:
            segundo2= segundo.siguiente    
            if actual.Dato._tiempo != segundo.Dato._tiempo:
                
                print("Tempo1:", actual.Dato._tiempo, "tempo2:", segundo.Dato._tiempo)
                print("Dato1:", actual.Dato._dato, "Dato2:", segundo.Dato._dato)
                
                # if grupoValido:
                #     print(actual.Dato._dato, end="")
                #     if actual.siguiente:  # Solo imprime la flecha si hay un nodo siguiente
                #         print(" -> ", end="")
                #     print(segundo.Dato._dato, end="")                        
                #     print(" = ", (actual.Dato._dato+segundo.Dato._dato), end="")
                #     print("")
                if primerDatoMismoTiempo is None and actual.Dato._tiempo == tiempoAnterior:
                    primerDatoMismoTiempo = actual  # Guardar el primer dato con el mismo tiempo
                actual = actual.siguiente
                if actual is None:
                    actual = primerDatoMismoTiempo  # Volver al primer dato con el mismo
                if tiempoAnterior is not None and actual.Dato._tiempo != tiempoAnterior:
                    actual = primerDatoMismoTiempo  # Volver al primer dato con el mismo tiempo
                    print("Regresé al primer dato con el mismo tiempo")
        
                
                
                # if actual.Dato._tiempo != tiempoAnterior and segundo2 != None:
                #    actual= self.primero
                #    print("Entro")
                       
            segundo = segundo.siguiente
            
        while actual is not None and actual.Dato._tiempo == tiempoAnterior:
            actual = actual.siguiente
        primerDatoMismoTiempo = actual

        if actual is not None:
            tiempoAnterior= actual.Dato._tiempo
            print("\nTiempo:", actual.Dato._tiempo)


  def generarMatrizPatrones(self):
    actual = self.primero
    segundo = self.primero
    print("Tiempo: ", actual.Dato._tiempo)
    while actual != None:

        segundo = segundo.siguiente
        if segundo != None:
            if actual.Dato._tiempo == segundo.Dato._tiempo:
                if actual.Dato._dato != 0:
                    print(1, end="")
                else:
                    print(0, end="")
                if actual.siguiente:  # Solo imprime la flecha si hay un nodo siguiente
                    print(" -> ", end="")
                actual = actual.siguiente
            else:
                if actual.Dato._dato != 0:
                    print(1, end="")
                else:
                    print(0, end="")
                print("")
                actual= actual.siguiente            
                print("Tiempo: ", actual.Dato._tiempo)
        else:
            if actual.Dato._dato != 0:
                print(1, end="")
            else:
                print(0, end="")
            actual = actual.siguiente
    print("")

    
    actual = self.primero
    segundo = self.primero
    tiempo_actual = -1  # Inicializar con un valor que no sea posible en tu caso
    fila_reducida_1 = 0
    fila_reducida_2 = 0
    fila_reducida_3 = 0
    fila_reducida_4 = 0

    while actual is not None:
        segundo = segundo.siguiente
        
        if segundo is not None:
            if actual.Dato._tiempo == segundo.Dato._tiempo:
                if tiempo_actual != actual.Dato._tiempo:
                    tiempo_actual = actual.Dato._tiempo
                    fila_reducida_1 = 0
                    fila_reducida_2 = 0
                    fila_reducida_3 = 0
                    fila_reducida_4 = 0

                fila_reducida_1 += actual.Dato._dato
                fila_reducida_2 += actual.Dato._amplitud
                fila_reducida_3 += actual.Dato._dato  # Otra vez, para hacer la suma de 0 y 1
                fila_reducida_4 += actual.Dato._amplitud  # Otra vez, para hacer la suma de 0 y 1
                actual = actual.siguiente
            else:
                if tiempo_actual != actual.Dato._tiempo:
                    tiempo_actual = actual.Dato._tiempo
                    print(fila_reducida_1, fila_reducida_2, fila_reducida_3, fila_reducida_4)
                    fila_reducida_1 = 0
                    fila_reducida_2 = 0
                    fila_reducida_3 = 0
                    fila_reducida_4 = 0
                
                fila_reducida_1 += actual.Dato._dato
                fila_reducida_2 += actual.Dato._amplitud
                fila_reducida_3 += actual.Dato._dato
                fila_reducida_4 += actual.Dato._amplitud
                
                actual = actual.siguiente
        
        else:
            if tiempo_actual != actual.Dato._tiempo:
                tiempo_actual = actual.Dato._tiempo
                print(fila_reducida_1, fila_reducida_2, fila_reducida_3, fila_reducida_4)
                fila_reducida_1 = 0
                fila_reducida_2 = 0
                fila_reducida_3 = 0
                fila_reducida_4 = 0
            
            fila_reducida_1 += actual.Dato._dato
            fila_reducida_2 += actual.Dato._amplitud
            fila_reducida_3 += actual.Dato._dato
            fila_reducida_4 += actual.Dato._amplitud
            
            actual = actual.siguiente

    actual = self.primero
    segundo = self.primero
    tiempo_actual = -1  # Inicializar con un valor que no sea posible en tu caso

    while actual is not None:
        segundo = segundo.siguiente
        
        if segundo is not None:
            if actual.Dato._tiempo == segundo.Dato._tiempo:
                if tiempo_actual != actual.Dato._tiempo:
                    tiempo_actual = actual.Dato._tiempo
                    print("\nGrupo:", end=" ")
                print(actual.Dato._dato, end=" ")
                actual = actual.siguiente
            else:
                if tiempo_actual != actual.Dato._tiempo:
                    tiempo_actual = actual.Dato._tiempo
                    print("\nGrupo:", end=" ")
                print(actual.Dato._dato)
                actual = actual.siguiente
        
        else:
            if tiempo_actual != actual.Dato._tiempo:
                tiempo_actual = actual.Dato._tiempo
                print("\nGrupo:", end=" ")
            print(actual.Dato._dato)
            actual = actual.siguiente
  
  def generarMatrizR(self):
    cantidad_tiempos = self.contar_elementos()
    actual = self.primero
    
    for tiempo1 in range(1, cantidad_tiempos + 1):
        segundo = self.primero  
        for tiempo2 in range(tiempo1, cantidad_tiempos + 1):
            grupo_valido = True 
            
            if segundo is not None and actual is not None:  # Asegurarse de que ambos nodos sean válidos
                if actual.Dato._tiempo != segundo.Dato._tiempo:
                    print("Tmp1:", actual.Dato._tiempo, "Tmp2:", segundo.Dato._tiempo)
                segundo = segundo.siguiente
            else:
                break  # Si alguno de los nodos es None, no hay necesidad de seguir
            
        actual = actual.siguiente    

    

# Llamar al método generarMatrizR



# Llamar al método generarMatrizR
   
  def contarTiempos(self):      
    actual = self.primero
    count = 1
    while actual is not None:
        segundo = actual.siguiente
        
        if segundo is not None and actual.Dato._tiempo != segundo.Dato._tiempo:
            count += 1
        
        actual = actual.siguiente
            
    print("Cantidad de tiempos:", count)
    return count


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