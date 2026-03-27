import tkinter as tk
from tkinter import messagebox

#Variables globales para el manejo de ventanas
Ventana_Num = None
ventana_Info = None
ventana_ani = None
contador = 0

#Funcion que verifica si hay ventanas abiertas
def esta_abierta(v):
    return v is not None and v.winfo_exists() #verifica si la ventana está abierta o si fué cerrada

#Funcion para la ventana de analisis
def crear_ventana_Num():
    global Ventana_Num, contador      
    Ventana_Num = tk.Toplevel(menu)             #Configuracion de la ventana de analisis
    Ventana_Num.title("Análisis de números")
    Ventana_Num.geometry("600x500")
    Ventana_Num.resizable(False, False)
    Ventana_Num.protocol("WM_DELETE_WINDOW", cerrar_ventana_Num)   #Manejo de ventanas
    contador += 1    #Contador de ventana abierta

 #Canva de la ventana de análisis
    canva_num = tk.Canvas(Ventana_Num, width=600, height=500, bg="white")
    canva_num.pack()

    resultado_var = tk.StringVar()
    resultado_var.set("")


    def pares_producto(n, a=1):
     if a > n // a:                      # si a > b, se detiene
        return ""
     elif n % a == 0:                    # si a es divisor exacto
        return f"({a}, {n // a})   " + pares_producto(n, a + 1)
     else:                               # si no es divisor, salta al siguiente
        return pares_producto(n, a + 1)                               # si a > b, se detiene
        

    def analizar():
     texto = entrada.get()
     es_numero = texto.isdigit()
     if not es_numero:
        messagebox.showerror("Error", "Ingresa solo números enteros positivos.")
     elif int(texto) <= 0:
        messagebox.showerror("Error", "El número debe ser mayor que 0.")
     else:
        resultado_var.set(pares_producto(int(texto)))

 #Texto de análisis
    Analisis = tk.Label(canva_num, text="Análisis de números ", background="white", font=("verdana", 18, "bold"))
    Analisis.place(x=150, y=10)

  #Texto de ingresar el número
    ingresar = tk.Label(canva_num, text="Ingresa un número entero positivo:", bg="white", font=("verdana", 11))
    ingresar.place(x=100, y=80)

 #Espacio para ingresar el número
    entrada = tk.Entry(canva_num, font=("verdana", 11), width=10)
    entrada.place(x=300, y=80)

 #Boton para analizar el número ingresado
    b_anali = tk.Button(canva_num, text="Analizar", command=lambda: analizar(), font=("verdana", 11))
    b_anali.place(x=250, y=130)
 
 #Texto que indica dónde va a aparecer el resultado
    result = tk.Label(canva_num, text="Pares encontrados:", bg="white", font=("verdana", 11))
    result.place(x=100, y=190)
 
 #Resultado obtenido
    resultado_label = tk.Label(canva_num, textvariable=resultado_var, bg="white", font=("verdana", 11), wraplength=500, justify="left")
    resultado_label.place(x=50, y=230)


 #Boton para volver al menú
    Volver_M = tk.Button(canva_num, text="Volver al Menú", command=lambda:cerrar_ventana_Num())
    Volver_M.place(x=250, y=400)

#Funcion para abir la ventana de análisi
def abrir_ventana_Num():
     if esta_abierta(Ventana_Num):
        Ventana_Num.lift()
     elif contador >= 1:
        messagebox.showwarning("Límite", "Máximo 2 ventanas abiertas.")
     else:
        crear_ventana_Num()

#Funcion para volver al menú y cerrar la ventana de análisis
def cerrar_ventana_Num():
    global Ventana_Num, contador
    Ventana_Num.destroy()
    Ventana_Num = None
    contador -= 1   #Disminución en el contador
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


menu.mainloop()