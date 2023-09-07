import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog
from Dato import Dato
from Señal import Señal
import SG as sg
import ListaEnlazada as lista
from Graph import Graph
from xml.dom import minidom

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
        actual.Señal._listaEntrada.generarMatrizReducida(actual.Señal._listaSalida)

        actual = actual.siguiente

def generarGrafica(nSeñal):
        actual = sg.listaSeñales.obtener_señal_por_posicion(nSeñal)

        print("Se comienza a generar la grafica")
        print("")
        graph = Graph()

        graph.graficar(actual._listaEntrada, actual._tiempo, actual._amplitud, actual._nombre)
        print("Se comienza a generar la grafica reducida")
        graph = Graph()
        graph.graficarMatrizReducida(actual._listaSalida, actual._amplitud, actual._nombre)
        print("-------------------------")
        print("")

def escribir_archivo_salida():
    # Crear una ventana tkinter (puedes ocultarla si lo prefieres)
    root2 = tk.Tk()
    root2.withdraw()  # Ocultar la ventana principal de tkinter

    root = ET.Element("senalesReducidas")
    actual = sg.listaSeñales.primero
    while actual is not None:
        señal_element = ET.SubElement(root, "senal")
        señal_element.set("nombre", actual.Señal._nombre)
        señal_element.set("A", str(actual.Señal._amplitud))
        listaReducida = actual.Señal._listaSalida
        
        count = 0
        tiempo_actual = None
        grupo_element = None
        tiempos_element = None
        datos_grupo_element = None
        
        actualLista = listaReducida.primero
        while actualLista is not None:
            if actualLista.Dato._tiempo != tiempo_actual:
                if grupo_element is not None:
                    señal_element.append(grupo_element)
                grupo_element = ET.Element("grupo")
                grupo_element.set("g", str(actualLista.Dato._grupo))
                tiempos_element = ET.Element("tiempos")
                tiempos_element.text = actualLista.Dato._tiempo
                grupo_element.append(tiempos_element)
                datos_grupo_element = ET.Element("datosGrupo")
                grupo_element.append(datos_grupo_element)
                tiempo_actual = actualLista.Dato._tiempo
            
            dato_element = ET.Element("dato")
            dato_element.set("A", str(actualLista.Dato._amplitud))
            dato_element.text = str(actualLista.Dato._dato)
            datos_grupo_element.append(dato_element)
            
            actualLista = actualLista.siguiente
        
        if grupo_element is not None:
            señal_element.append(grupo_element)
        
        actual = actual.siguiente
    
    # Obtener la carpeta de destino del usuario
    carpeta_destino = filedialog.askdirectory(title="Seleccione la carpeta de destino")

    if not carpeta_destino:
        print("No se seleccionó ninguna carpeta de destino.")
        return

    # Crear la ruta completa del archivo de salida
    ruta_archivo_salida = f"{carpeta_destino}/salida.xml"

    # Crear y formatear la salida XML
    xml_string = ET.tostring(root, encoding="utf-8")
    xml_pretty = minidom.parseString(xml_string).toprettyxml(indent="  ")

    # Escribir el archivo XML en la carpeta seleccionada
    with open(ruta_archivo_salida, "w") as archivo_xml:
        archivo_xml.write(xml_pretty)

    print(f"Archivo XML de salida creado con éxito en: {ruta_archivo_salida}")







