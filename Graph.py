import graphviz
import SG as sg
from Dato import Dato 

class Graph:
    def __init__(self):
        self.dot = graphviz.Digraph('structs', filename='structs.gv', node_attr={'shape': 'record', 'fontname':'Helvetica'})
        
    def graficar(self, listaEntrada, tiempoTotal, AmplitudTotal, nombreSeñal):
        sg.listaTemp.limpiarTodo()
        sg.listaTemp2.limpiarTodo()
        # Obtener el nombre de la señal
        nombre_senal = nombreSeñal
        # Crear un nodo para la señal en el gráfico
        self.dot.node(nombre_senal, label=nombre_senal)

        # Inicializar variable para el seguimiento del último nodo de tiempo
        ultimo_nodo_tiempo = nombre_senal

        # Recorrer la lista de entrada y agregar los nodos de tiempo y datos
        actual = listaEntrada.primero
        cantidadTiempos = listaEntrada.contarTiempos()
        count = 0
        nodo_dato="t="+str(tiempoTotal)
        self.dot.edge(ultimo_nodo_tiempo, nodo_dato)
        nodo_dato="A="+str(AmplitudTotal)
        self.dot.edge(ultimo_nodo_tiempo, nodo_dato)
        countInterno=0
        while count < cantidadTiempos:
            actual = listaEntrada.primero
            count +=1
            espaciadoTexto=""
            while actual is not None:
                if actual.Dato._tiempo == count:
                    if count ==1:
                        countInterno+=1
                        tiempo = actual.Dato._tiempo
                        amplitud = actual.Dato._amplitud
                        valor = actual.Dato._dato
                        # Crear un nodo para el tiempo en el gráfico
                        nodo_tiempo = f"t{tiempo}"
                        # Crear un nodo para el dato en el gráfico
                        nodo_dato = f"t{espaciadoTexto+str(tiempo)}_Valor{valor}"
                        
                        if sg.listaTemp.buscar_dato(actual.Dato._tiempo) != True:
                            espaciadoTexto= espaciadoTexto+" "
                            datoTemp_obj = Dato(nodo_dato,(espaciadoTexto+str(actual.Dato._tiempo)), "", str(countInterno))
                            sg.listaTemp.insertar(datoTemp_obj)
                        else:
                            datoTemp_obj = Dato(nodo_dato,str(actual.Dato._tiempo), "", "")
                            sg.listaTemp.insertar(datoTemp_obj)
                        
                        # Conectar el último nodos del primero tiempo al nombre de la señal
                        self.dot.edge(ultimo_nodo_tiempo, nodo_dato)
                    else:

                        tiempo = actual.Dato._tiempo
                        amplitud = actual.Dato._amplitud
                        valor = actual.Dato._dato
                        nodo_dato = f"t{espaciadoTexto+str(tiempo)}_Valor{valor}"
                        ultimo_nodo_tiempo = sg.listaTemp.obtener_primer_dato()                   

                        if sg.listaTemp2.buscar_dato(actual.Dato._tiempo) != True:
                            espaciadoTexto= espaciadoTexto+" "
                            nodo_dato = f"t{espaciadoTexto+str(tiempo)}_Valor{valor}"
                            datoTemp_obj = Dato(nodo_dato, actual.Dato._tiempo, "", "")
                            sg.listaTemp2.insertar(datoTemp_obj)
                        else:
                            datoTemp_obj = Dato(nodo_dato, actual.Dato._tiempo, "", "")
                            sg.listaTemp2.insertar(datoTemp_obj)
                        
                        self.dot.edge(ultimo_nodo_tiempo, nodo_dato)
                        
                        sg.listaTemp.eliminar_primer_dato()
                    
                # Conectar el nodo de tiempo actual al nodo de dato actual
                ##self.dot.edge(ultimo_nodo_tiempo, nodo_dato)
            
                # Actualizar el último nodo de tiempo
                # ultimo_nodo_tiempo = nodo_tiempo
            
                actual = actual.siguiente
            
            if count>1:
                sg.listaTemp= sg.listaTemp2

            # Generar la imagen del gráfico
        nombreArchivo = 'img/frecuencia-'+str(nombreSeñal)+'.png'
        self.dot.render(outfile=nombreArchivo).replace('\\', '/')

    def graficarMatrizReducida(self, listaReducida, AmplitudTotal, nombreSeñal):
        sg.listaTemp.limpiarTodo()
        sg.listaTemp2.limpiarTodo()
        # Obtener el nombre de la señal
        nombre_senal = nombreSeñal
        # Crear un nodo para la señal en el gráfico
        self.dot.node(nombre_senal, label=nombre_senal)

        # Inicializar variable para el seguimiento del último nodo de tiempo
        ultimo_nodo_tiempo = nombre_senal

        # Recorrer la lista de entrada y agregar los nodos de tiempo y datos
        actual = listaReducida.primero
        cantidadTiempos = listaReducida.contarTiempos()
        count = 0
        nodo_dato="A="+str(AmplitudTotal)
        self.dot.edge(ultimo_nodo_tiempo, nodo_dato)
        espaciadoTexto=""
        nodo_datoGrupo=""
        while count < cantidadTiempos:
            actual = listaReducida.primero
            count +=1
            count2=count-1
            
            while actual is not None:
                if actual.Dato._grupo == count:
                    if count ==1:
                        tiempo = actual.Dato._tiempo
                        amplitud = actual.Dato._amplitud
                        valor = actual.Dato._dato
                        # Crear un nodo para el tiempo en el gráfico
                        if count2 <count:
                            nodo_datoGrupo="G="+str(count)+" (t="+str(tiempo)+")"
                            self.dot.edge(ultimo_nodo_tiempo, nodo_datoGrupo)            
                        count2 +=1
                        nodo_tiempo = f"t{tiempo}"
                        # Crear un nodo para el dato en el gráfico
                        nodo_dato = f"{espaciadoTexto+str(valor)}"
                        if sg.listaTemp.buscar_dato(actual.Dato._tiempo) != True:
                            espaciadoTexto= espaciadoTexto+" "
                            datoTemp_obj = Dato(nodo_dato,(espaciadoTexto+str(actual.Dato._tiempo)), "", "")
                            sg.listaTemp.insertar(datoTemp_obj)
                        else:
                            datoTemp_obj = Dato(nodo_dato,str(actual.Dato._tiempo), "", "")
                            sg.listaTemp.insertar(datoTemp_obj)
                        
                        # Conectar el último nodos del primero tiempo al nombre de la señal
                        self.dot.edge(ultimo_nodo_tiempo, nodo_dato)
                    else:
                        
                        tiempo = actual.Dato._tiempo
                        amplitud = actual.Dato._amplitud
                        
                        if count2 <count:
                            ultimo_nodo_tiempo=nodo_datoGrupo
                            nodo_datoGrupo="G="+str(count)+" (t="+str(tiempo)+")"
                            self.dot.edge(ultimo_nodo_tiempo, nodo_datoGrupo)    
                            count2 +=1        

                        valor = actual.Dato._dato
                        nodo_dato = f"{espaciadoTexto+str(valor)}"
                        ultimo_nodo_tiempo = sg.listaTemp.obtener_primer_dato()                   
                        
                        if sg.listaTemp2.buscar_dato(actual.Dato._tiempo) != True:
                            espaciadoTexto= espaciadoTexto+" "
                            nodo_dato = f"{espaciadoTexto+str(valor)}"
                            datoTemp_obj = Dato(nodo_dato, actual.Dato._tiempo, "", "")
                            sg.listaTemp2.insertar(datoTemp_obj)
                        else:
                            datoTemp_obj = Dato(nodo_dato, actual.Dato._tiempo, "", "")
                            sg.listaTemp2.insertar(datoTemp_obj)
                        
                        self.dot.edge(ultimo_nodo_tiempo, nodo_dato)
                        
                        sg.listaTemp.eliminar_primer_dato()
                    

                actual = actual.siguiente
            
            if count>1:
                sg.listaTemp= sg.listaTemp2

            # Generar la imagen del gráfico
        nombreArchivo = 'img/reducida-'+str(nombreSeñal)+'.png'
        self.dot.render(outfile=nombreArchivo).replace('\\', '/')
