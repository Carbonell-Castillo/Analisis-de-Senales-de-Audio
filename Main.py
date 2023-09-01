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
                print("No existen productos en existencia")
            else:
                logic.procesarArchivo()
        
        elif option == 3:
            if sg.listaProductos.esta_vacia():
                print("No existen productos en existencia")
            else:
                sg.listaProductos.generar_reporte("Reporte.txt")

        elif option == 4:
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")