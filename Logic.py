import xml.etree.ElementTree as ET
from Dato import Dato
from Señal import Señal
import SG as sg
import ListaEnlazada as lista
from Graph import Graph

def validar_tiempo_amplitud(tiempo, amplitud, signal_t, signal_a):
    if tiempo < 1 or tiempo > signal_t:
        raise ValueError(f"Valor de tiempo inválido en dato: {tiempo}")
    if amplitud < 1 or amplitud > signal_a:
        raise ValueError(f"Valor de amplitud inválido en dato: {amplitud}")
        

def leerEntrada(xml_file):
    try:
        tree = ET.parse(xml_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se pudo encontrar el archivo: {xml_file}")
    
    root = tree.getroot()

    for senal_element in root.findall('.//senal'):
        listaEntrada = lista.lista_enlazada()
        listaMatrizReducida = lista.lista_enlazada()
        nombre = senal_element.get('nombre')
        tiempo_total = int(senal_element.get('t'))
        amplitud_total = int(senal_element.get('A'))
        if (tiempo_total>0 and tiempo_total<=3600) and (amplitud_total>0 and amplitud_total<=130):
            for dato_element in senal_element.findall('.//dato'):
                tiempo = int(dato_element.get('t'))
                amplitud = int(dato_element.get('A'))
                valor = int(dato_element.text)
                validar_tiempo_amplitud(tiempo, amplitud, tiempo_total, amplitud_total)
                dato_obj = Dato("",tiempo, amplitud, valor)
                listaEntrada.insertar(dato_obj)

            print(f"Señal: {nombre}")
            señal_obj= Señal(nombre,tiempo_total, amplitud_total, listaEntrada, listaMatrizReducida)
            sg.listaSeñales.insertar(señal_obj)
    sg.listaSeñales.recorrer()
    # for dato_element in root.findall('.//dato'):
    #     tiempo = int(dato_element.get('t'))
    #     amplitud = int(dato_element.get('A'))
    #     dato = int(dato_element.text)
    #     dato_obj = Dato("", tiempo, amplitud, dato)
    #     sg.listaEntrada.insertar(dato_obj)
    
    # sg.listaEntrada.recorrer()

def procesarArchivo():
    print("Se comienza a procesar el archivo: ", sg.rutaArchivo)    
    ##Se crea la matriz respectiva
    ##Se obtiene la cantidad de señales.
    actual = sg.listaSeñales.primero
    while actual is not None:
        print("")
        print("-------------------------")
        print("Se comienza a generar la matriz de frecuencia - Señal:", actual.Señal._nombre)
        print("")
        actual.Señal._listaEntrada.generarMatrizFrecuencia()
        print("")
        print("Se comienza a generar la matriz de patrones: ")
        actual.Señal._listaEntrada.generarMatrizPatrones()
        print("")
        print("Se comienza a generar la matriz reducida")
        actual.Señal._listaEntrada.gene2(actual.Señal._listaSalida)

        print("Se comienza a generar la grafica")
        print("")
        actual.Señal._listaSalida.recorrerMatrizReducida()
        graph = Graph()
        graph.graficar(actual.Señal._listaEntrada, actual.Señal._tiempo, actual.Señal._amplitud, actual.Señal._nombre)
        # print("Se comienza a generar la grafica reducida")
        # graph = Graph()
        # graph.graficarMatrizReducida(actual.Señal._listaSalida, actual.Señal._amplitud, actual.Señal._nombre)
        print("-------------------------")
        print("")

        sg.listaTiempos.limpiar()
        actual = actual.siguiente
        
    # sg.listaEntrada.generarMatrizFrecuencia()
    # print("Se comienza a generar la matriz de patrones: ")
    # sg.listaEntrada.generarMatrizPatrones()
    # print("Se comienza a generar la matriz reducida")
    # sg.listaEntrada.contarTiempos()
    # sg.listaEntrada.gene2()





