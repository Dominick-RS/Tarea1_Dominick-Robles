import tkinter as tk
from tkinter import messagebox

#Variables globales para el manejo de ventanas
Ventana_Num = None
ventana_Info = None
ventana_ani = None
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
    Volver_M.place(x=250, y=400)

#Funcion para abir la ventana de análisi
def abrir_ventana_Num():
    esta_abierta(Ventana_Num) and Ventana_Num.lift()
    (not esta_abierta(Ventana_Num)) and (contador >= 1) and messagebox.showwarning("Límite", "Máximo 2 ventanas abiertas.")
    (not esta_abierta(Ventana_Num)) and (contador < 1) and crear_ventana_Num()

#Funcion para volver al menú y cerrar la ventana de análisis
def cerrar_ventana_Num():
    global Ventana_Num, contador
    Ventana_Num.destroy()
    Ventana_Num = None
    contador -= 1   #Disminución en el contador
    menu.lift()


#Funcion para crear la ventana de información
def crear_ventana_Info():
    global ventana_Info, contador
    ventana_Info = tk.Toplevel(menu)          #Configuración de la ventana información
    ventana_Info.title("Información")
    ventana_Info.geometry("600x500")
    ventana_Info.resizable(False, False)
    ventana_Info.protocol("WM_DELETE_WINDOW", cerrar_ventana_Info)  #Manejo de ventanas
    contador += 1                               #Contador de ventana abierta

 #Canva de la ventana información
    canva_i = tk.Canvas(ventana_Info, width= 600, height= 500, bg="white")
    canva_i.pack()

 #Texto de información
    labeli = tk.Label(canva_i,text="información", background="white", font=("verdana", 18, "bold"))
    labeli.place(x=200, y= 10)

 #Boton para volver al menú
    Volver_i = tk.Button(canva_i, text="Volver al Menú", command=lambda:cerrar_ventana_Info())
    Volver_i.place(x=250, y=400 )

#Funcion para abir la ventana de información 
def abrir_ventana_Info():
    esta_abierta(ventana_Info) and ventana_Info.lift()
    (not esta_abierta(ventana_Info)) and (contador >= 1) and messagebox.showwarning("Límite", "Máximo 2 ventanas abiertas.")
    (not esta_abierta(ventana_Info)) and (contador < 1) and crear_ventana_Info()

#Funcion para cerrar la ventana de Información
def cerrar_ventana_Info():
    global ventana_Info, contador
    ventana_Info.destroy()
    ventana_Info = None
    contador -= 1
    menu.lift()

#Funcion para crear la ventana de la animación
def crear_ventana_ani():
    global ventana_ani, contador
    ventana_ani = tk.Toplevel(menu)      #Configuración de la ventana de animación
    ventana_ani.title("Animación")
    ventana_ani.geometry("600x500")
    ventana_ani.resizable(False, False)
    ventana_ani.protocol("WM_DELETE_WINDOW", cerrar_ventana_ani)
    contador += 1                        #Contador de ventana abierta

 
    #canva para la ventana de animación
    canva_a = tk.Canvas(ventana_ani, width= 600, height= 500, bg="white")
    canva_a.pack()

    #Texto de la ventana animacion
    labela = tk.Label(canva_a, text="Animación", bg="white", font=("verdana", 18, "bold"))
    labela.place(x=230, y= 10)

    #Boton para regresar al menú
    volver_a = tk.Button(canva_a, text="Volver al Menú", command=lambda: cerrar_ventana_ani())
    volver_a.place(x=230, y=450)

#Funcion para abrir la ventana de animación
def abrir_ventana_ani():
    esta_abierta(ventana_ani) and ventana_ani.lift()
    (not esta_abierta(ventana_ani)) and (contador >= 1) and messagebox.showwarning("Límite", "Máximo 2 ventanas abiertas.")
    (not esta_abierta(ventana_ani)) and (contador < 1) and crear_ventana_ani()

#Funcion para cerrar la ventana
def cerrar_ventana_ani():
    global ventana_ani, contador
    ventana_ani.destroy()
    ventana_ani = None
    contador -= 1
    menu.lift()

#Configuracion del menú
menu = tk.Tk()
menu.title ("Menú")
menu.geometry("600x600")
menu.resizable(width=False, height=False)

#Texto del menu
labelm = tk.Label(menu, text="Menú", font=("Verdana", 20, "bold"))
labelm.pack(pady=10)

#Canva del menu
canva_m = tk.Canvas(menu, width=800, height=600, bg="white")
canva_m.pack()

#Boton para abrir el análisis de números
AnalizarN = tk.Button(canva_m, text="Abrir análisis de números", width=20, command=lambda: abrir_ventana_Num())
AnalizarN.place(x=20, y=20)

#Boton para ver la información personal
Infor = tk.Button(canva_m, text="Mostrar información", width=20, command=lambda: abrir_ventana_Info())
Infor.place(x=230, y=20)

#Boton para abrir la ventana de animación
anim = tk.Button(canva_m, text="Animación", width=20, command=lambda: abrir_ventana_ani())
anim.place(x=430, y=20)

menu.mainloop()
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