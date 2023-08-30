import tkinter as tk
from tkinter import filedialog
import SG as sg ##Super global



if __name__ == "__main__":
    
    while True:
        option = sg.showMenu()

        if option == 1:
            inventario_inicial = sg.open_file()        
            if inventario_inicial:
                print("Cargando Inventario inicial desde:", inventario_inicial)
                logic.leer_inventario(inventario_inicial)

        elif option == 2:
            instrucciones_movimientos = sg.open_file()
            if sg.listaProductos.esta_vacia():
                print("No existen productos en existencia")
            elif instrucciones_movimientos:
                print("Cargando Instrucciones de movimientos desde:", instrucciones_movimientos)
                logic.leer_movimientos(instrucciones_movimientos)
        
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