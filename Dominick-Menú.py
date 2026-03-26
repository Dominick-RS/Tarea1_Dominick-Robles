import tkinter as tk
from tkinter import messagebox

#Variables globales para el manejo de ventanas
Ventana_Num = None
ventana_Info = None
ventana_Ani = None
contador = 0

#Funcion que verifica si hay ventanas abiertas
def esta_abierta(v):
    return v is not None and v.winfo_exists()

#Funcion para la ventana de analisis
def crear_ventana_Num():
    global Ventana_Num, contador
    Ventana_Num = tk.Toplevel(menu)                  #Configuracion de la ventana de analisis
    Ventana_Num.title("Análisis de números")
    Ventana_Num.geometry("600x500")
    Ventana_Num.resizable(False, False)
    Ventana_Num.protocol("WM_DELETE_WINDOW", cerrar_ventana_Num)   #Manejo de ventanas
    contador += 1    #Contador de ventana abierta

 #Canva de la ventana de análisis
    canva_num = tk.Canvas(Ventana_Num, width=600, height=500, bg="white")
    canva_num.pack()

 #Texto de análisis
    Analisis = tk.Label(canva_num, text="Análisis de números ", background="white", font=("verdana", 18, "bold"))
    Analisis.place(x=150, y=10)

 #Boton para volver al menú
    Volver_M = tk.Button(canva_num, text="Volver al Menú", command=lambda:cerrar_ventana_Num())
    Volver_M.place(x=250, y=400 )

#Funcion para abir la ventana de análisi
def abrir_ventana_Num():
    esta_abierta(Ventana_Num) and Ventana_Num.lift()
    (not esta_abierta(Ventana_Num)) and (contador >= 2) and messagebox.showwarning("Límite", "Máximo 2 ventanas abiertas.")
    (not esta_abierta(Ventana_Num)) and (contador < 2) and crear_ventana_Num()

#Funcion para volver al menú y cerrar la ventana de análisis
def cerrar_ventana_Num():
    global Ventana_Num, contador
    Ventana_Num.destroy()
    Ventana_Num = None
    contador -= 1   #Disminución en el contador
    menu.lift()

#Configuracion del menu
menu = tk.Tk()
menu.title ("Menú")
menu.geometry("600x600")
menu.resizable(width=False, height=False)

#Texto del menu
label = tk.Label(menu, text="Menú", font=("Verdana", 20, "bold"))
label.pack(pady=10)

#Canva del menu
canva_m = tk.Canvas(menu, width=800, height=600, bg="white")
canva_m.pack()

#Boton para abrir el analisis de números
AnalizarN = tk.Button(canva_m, text="Abrir análisis de números", width=20, command=lambda: abrir_ventana_Num())
AnalizarN.place(x=20, y= 20)


menu.mainloop()