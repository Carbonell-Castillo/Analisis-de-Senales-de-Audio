import xml.etree.ElementTree as ET
from Dato import Dato
import SG as sg

def leerEntrada(xml_file):
    try:
        tree = ET.parse(xml_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se pudo encontrar el archivo: {xml_file}")
    
    root = tree.getroot()

    for dato_element in root.findall('.//dato'):
        tiempo = int(dato_element.get('t'))
        amplitud = int(dato_element.get('A'))
        dato = int(dato_element.text)
        dato_obj = Dato(tiempo, amplitud, dato)
        sg.listaEntrada.insertar(dato_obj)
    
    sg.listaEntrada.recorrer()

def procesarArchivo():
    print("Se comienza a procesar el archivo: ", sg.rutaArchivo)    
    ##Se crea la matriz respectiva
    print("Se comienza a generar la matriz de frecuencia: ")
    sg.listaEntrada.recorrer3()
    print("Se comienza a generar la matriz de patrones: ")
    sg.listaEntrada.generarMatrizPatrones()





