import tkinter as tk 
from tkinter import filedialog 

def showMenu():
    while True:
        print("-------------------------------------------------")
        print("Proyecto No 1 IPC 2")
        print("-------------------------------------------------")
        print("# Menu Principal\n")
        print("1. Cargar archivo")
        print("2. Procesar archivo salida")
        print("3. Escribir archivo salida")
        print("4. Mostrar datos del estudiante")
        print("5. Generar grafica")
        print("6. inicializar sistema")
        print("7. Salida\n")

        try:
            option = int(input("Ingrese una opción: "))
            if 1 <= option <= 4:
                return option
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Opción inválida. Intente nuevamente.")