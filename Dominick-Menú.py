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

#Configuracion del menu
menu = tk.Tk()
menu.title ("Menú")
menu.geometry("800x600")
menu.resizable(width=False, height=False)

#Texto del menu
label = tk.Label(menu, text="Menú", font=("Verdana", 20, "bold"))
label.pack(pady=10)

#Canva del menu
canva_m = tk.Canvas(menu, width=800, height=600, bg="white")
canva_m.pack()


menu.mainloop()