from Dato import Dato
from Tiempo import Tiempo
import SG as sg
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

  def recorrerMatrizReducida(self):
    actual = self.primero
    print("Datos: \n")
    print("----------------------------------------------------------------------------")
    while actual != None:
      print("Grupo: ", actual.Dato._grupo, " Tiempo: ", actual.Dato._tiempo, " Amplitud: ", actual.Dato._amplitud, " Dato: ", actual.Dato._dato)
      actual = actual.siguiente
    print("----------------------------------------------------------------------------")
 
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
    terminaFila=False
    count=1
    count2=0
    salida=""
    estado = False
    while actual is not None:
        segundo = self.primero
        salida=""
        while segundo is not None:
            segundo2= segundo.siguiente    
            if actual.Dato._tiempo != segundo.Dato._tiempo:
                
                print("Tempo1:", actual.Dato._tiempo, "tempo2:", segundo.Dato._tiempo)
                print("Dato1:", actual.Dato._dato, "Dato2:", segundo.Dato._dato)
                
                if actual.Dato._dato !=0 and segundo.Dato._dato !=0:
                    
                    salida= salida+ str(actual.Dato._dato+segundo.Dato._dato)+ "->"
                    tempTiempo= str(actual.Dato._tiempo)+ ","+ str(segundo.Dato._tiempo)
                    tempTiempo2= str(segundo.Dato._tiempo)+ ","+ str(actual.Dato._tiempo)
                    
                    print("TIempo temporal: ", tempTiempo)
                    if sg.listaMatrizReducida.buscar_dato(tempTiempo2):
                        dato_obj = Dato(count, tempTiempo, actual.Dato._amplitud, (actual.Dato._dato+segundo.Dato._dato))
                        sg.listaMatrizReducida.insertar(dato_obj)
                        print("Se aguardo: "+ str(actual.Dato._dato))
                        count2 +=1
                        grupoValido= True
                    else:
                        grupoValido= False
                        print("Se encontro")
                elif actual.Dato._dato ==0 and segundo.Dato._dato ==0:
                    
                    salida= salida + "->"+str(actual.Dato._dato)
                    tempTiempo= str(actual.Dato._tiempo)+ ","+ str(segundo.Dato._tiempo)
                    tempTiempo2= str(segundo.Dato._tiempo)+ ","+ str(actual.Dato._tiempo)
                    print("TIempo temporal: ", tempTiempo)
                    if sg.listaMatrizReducida.buscar_dato(tempTiempo2):
                        dato_obj = Dato(count, tempTiempo, actual.Dato._amplitud, (actual.Dato._dato+segundo.Dato._dato))
                        sg.listaMatrizReducida.insertar(dato_obj)
                        count2 +=1
                        grupoValido= True
                    else:
                        grupoValido= False
                        print("Se encontro")
                else:
                    grupoValido= False
                    estado= True
                # if grupoValido:
                #     print(actual.Dato._dato, end="")
                #     if actual.siguiente:  # Solo imprime la flecha si hay un nodo siguiente
                #         print(" -> ", end="")
                #     print(segundo.Dato._dato, end="")                        
                #     print(" = ", (actual.Dato._dato+segundo.Dato._dato), end="")
                #     print("")
                if primerDatoMismoTiempo is None and actual.Dato._tiempo == tiempoAnterior:
                    primerDatoMismoTiempo = actual  # Guardar el primer dato con el mismo tiempo
                tiempo_actual = actual.Dato._tiempo

                actual = actual.siguiente
                
                if actual is None:
                    actual = primerDatoMismoTiempo  # Volver al primer dato con el mismo
                    if estado is False:
                        print("----Grupo encontrado----")
                        print("Grupo tiempo: ", actual.Dato._tiempo, " y ", segundo.Dato._tiempo)
                        print(salida)
                        print("-----------.---")
                        if grupoValido is True:
                            count +=1
                            tiempo_actual_insertar= Tiempo(tiempo_actual)
                            sg.listaTiempos.insertar(tiempo_actual_insertar)
                            tiempo_segundo = Tiempo(segundo.Dato._tiempo)
                            sg.listaTiempos.insertar(tiempo_segundo)
                            sg.listaEntrada.tiempo_modificar(tiempo_actual, "GEncontrado")
                            sg.listaEntrada.tiempo_modificar(segundo.Dato._tiempo, "GEncontrado")
                        salida=""
                        count2=0
                        grupoValido= False
                    else:
                        sg.listaMatrizReducida.limpiar(count2)
                        salida=""
                        estado= False
                        count2=0
                        
                if tiempoAnterior is not None and actual.Dato._tiempo != tiempoAnterior:
                    if estado is False:
                        print("----Grupo encontrado----")
                        print("Grupo tiempo: ", actual.Dato._tiempo, " y ", segundo.Dato._tiempo)
                        print(salida)
                        print("---------------")
                        if grupoValido is True:
                            count +=1
                            tiempo_actual_insertar= Tiempo(tiempo_actual)
                            sg.listaTiempos.insertar(tiempo_actual_insertar)
                            tiempo_segundo = Tiempo(segundo.Dato._tiempo)
                            sg.listaTiempos.insertar(tiempo_segundo)
                            sg.listaEntrada.tiempo_modificar(tiempo_actual, "GEncontrado")
                            sg.listaEntrada.tiempo_modificar(segundo.Dato._tiempo, "GEncontrado")
                        grupoValido=False
                        salida=""
                        count2=0
                    else:
                        sg.listaMatrizReducida.limpiar(count2)
                        salida=""
                        estado= False
                        count2=0
                    
                    actual = primerDatoMismoTiempo  # Volver al primer dato con el mismo tiempo
                    print("Regresé al primer dato con el mismo tiempo")
                    terminaFila=True                                
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
    countTiempos = count - 1
    print("C tiemo: " + str(countTiempos) + " 2: " + str(sg.listaEntrada.contarTiempos()))

    if countTiempos < sg.listaEntrada.contarTiempos():

        actual3 = self.primero
        # segundo3 = sg.listaTiempos.primero
        print("Tiempo: ", actual3.Dato._tiempo)
        countTiempoRecorrido=0
        while actual3 != None:
            if actual3.Dato._grupo == "":
                print("Entro221")
                tempTiempo2= str(actual3.Dato._tiempo)
                obj_restante = Dato(count, tempTiempo2, actual3.Dato._amplitud, (actual3.Dato._dato))
                sg.listaMatrizReducida.insertar(obj_restante)
                actual3= actual3.siguiente
                countTiempoRecorrido +=1
                if countTiempoRecorrido == sg.listaEntrada.cantidad_tiempos(actual3.Dato._tiempo):
                    count +=1
                    print("Se sumo: "+str(count))
            else:
                actual3 = actual3.siguiente
        print("")

    sg.listaMatrizReducida.recorrerMatrizReducida()
    sg.listaTiempos.recorrer()


  def tiempo_modificar(self,  tiempo_buscar, grupo):
    actual = self.primero
    while actual is not None:
        if actual.Dato._tiempo == tiempo_buscar:
            actual.Dato._grupo= grupo
        actual = actual.siguiente
  
  def cantidad_tiempos(self, tiempo_buscar):
    cantidad = 0
    actual = self.primero
    while actual is not None:
        if actual.Dato._tiempo == tiempo_buscar:
            cantidad +=1
        actual = actual.siguiente
    return cantidad
  
  def agregar_tiempos_faltantes(lista, total_tiempos):
    for i in range(1, total_tiempos + 1):
        tiempo_faltante = "Tiempo " + str(i)
        if not sg.listaMatrizReducida.tiempo_presente(tiempo_faltante):
            dato_obj = Dato(("Grupo "+str(lista.contarTiempos() + 1)), tiempo_faltante, 0, 0)
            lista.insertar(dato_obj)

  def buscar_dato(self, tiempo_buscar):
    actual = self.primero
    while actual is not None:
        if actual.Dato._tiempo == tiempo_buscar:
            return False
        actual = actual.siguiente
    return True
  
  def limpiar(self, cantidad):
        print("Se limpia")
        if cantidad <= 0:
            return  # No se necesita hacer nada si la cantidad es 0 o negativa

        if self.primero is None:
            return  # No hay elementos en la lista

        # Contar la cantidad total de nodos en la lista
        total_nodos = 0
        actual = self.primero
        while actual is not None:
            total_nodos += 1
            actual = actual.siguiente

        # Si la cantidad a borrar es mayor o igual al total de nodos, borra toda la lista
        if cantidad >= total_nodos:
            self.primero = None
            return

        # Mover hasta el nodo anterior al primero a eliminar
        nodo_anterior = None
        actual = self.primero
        for _ in range(total_nodos - cantidad):
            nodo_anterior = actual
            actual = actual.siguiente

        # Ahora actual es el primer nodo a eliminar
        if nodo_anterior is not None:
            nodo_anterior.siguiente = None
        else:
            self.primero = None

        # Liberar memoria de los nodos eliminados
        while actual is not None:
            temp = actual
            actual = actual.siguiente
            del temp  
    
  
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
