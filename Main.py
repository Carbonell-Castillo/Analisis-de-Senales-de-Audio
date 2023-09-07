import tkinter as tk
from tkinter import filedialog
import SG as sg ##Super global
import Logic as logic


if __name__ == "__main__":
    
    while True:
        option = sg.showMenu()

        if option == 1:
            archivo_entrada = sg.open_file()        
            if archivo_entrada:
                print("Cargando archivo de entrada desde:", archivo_entrada)
                logic.leerEntrada(archivo_entrada)

        elif option == 2:
            if sg.listaSeñales.esta_vacia():
                print("No existen Señales en existencia")
            else:
                logic.procesarArchivo()
        
        elif option == 3:
            if sg.listaSeñales.esta_vacia():
                print("No existen Señales en existencia")
            else:
                logic.escribir_archivo_salida()
        
        elif option == 4:
            print("Bruce Carbonell Castillo Cifuentes")
            print("202203069")
            print("Introduccion a la Programacion y computacion 2 Seccion N")
            print("Ingenieria en Ciencias y Sistemas")
            print("4to Semestre")

        elif option == 5:
            if sg.listaSeñales.esta_vacia():
                print("No existen Señales en existencia")
            else:
                suboption= sg.showSeñales()
                suboption=suboption-1
                logic.generarGrafica(suboption)
        elif option == 6:
            print("Inicializando sistema")
            archivo_entrada = sg.open_file()        
            if archivo_entrada:
                print("Cargando archivo de entrada desde:", archivo_entrada)
                logic.leerEntrada(archivo_entrada)
            
        elif option == 7:
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")