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
    if esta_abierta(ventana_Info):
        ventana_Info.lift()
    elif contador >= 1:      
        messagebox.showwarning("Límite", "Máximo 2 ventanas abiertas.")
    else:
        crear_ventana_Info()

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
    ventana_ani.geometry("600x530")
    ventana_ani.resizable(False, False)
    ventana_ani.protocol("WM_DELETE_WINDOW", cerrar_ventana_ani)
    contador += 1                        #Contador de ventana abierta

 
    #canva para la ventana de animación
    canva_a = tk.Canvas(ventana_ani, width= 600, height= 430, bg="white")
    canva_a.pack()

    r = 25  # radio de las esferas (hitbox)

    # Estado de las dos bolas: posición y velocidad
    estado = {
        "x1": 120.0,  "y1": 150.0,  "vx1": 4.0,  "vy1": 3.0,
        "x2": 420.0,  "y2": 280.0,  "vx2": -3.5, "vy2": -4.0 }

    # Límites de la caja (considerando el radio)
    IZQ = 10 + r
    DER = 590 - r
    ARR = 40 + r
    ABA = 420 - r


    # Lo que se ve de las esferas
    bola1 = canva_a.create_oval(
        estado["x1"]-r, estado["y1"]-r,
        estado["x1"]+r, estado["y1"]+r,
        fill="tomato", outline="darkred", width=2)
    
    bola2 = canva_a.create_oval(
        estado["x2"]-r, estado["y2"]-r,
        estado["x2"]+r, estado["y2"]+r,
        fill="royalblue", outline="darkblue", width=2)

    #Variable para cambiar la velocidad
    velocidad_var = tk.DoubleVar(value=1.0)

    #Fisicas y animación
    def actualizar():
        speed = velocidad_var.get()

        #Mover bolas según velocidad actual
        estado["x1"] += estado["vx1"] * speed
        estado["y1"] += estado["vy1"] * speed
        estado["x2"] += estado["vx2"] * speed
        estado["y2"] += estado["vy2"] * speed

        #Colisiones con bordes de la bola 1
        if estado["x1"] < IZQ:
            estado["x1"] = IZQ
            estado["vx1"] = abs(estado["vx1"])   # rebota hacia la derecha
        elif estado["x1"] > DER:
            estado["x1"] = DER
            estado["vx1"] = -abs(estado["vx1"])  # rebota hacia la izquierda

        if estado["y1"] < ARR:
            estado["y1"] = ARR
            estado["vy1"] = abs(estado["vy1"])   # rebota hacia abajo
        elif estado["y1"] > ABA:
            estado["y1"] = ABA
            estado["vy1"] = -abs(estado["vy1"])  # rebota hacia arriba

        #Closisiones con bordes de la bola 2
        if estado["x2"] < IZQ:
            estado["x2"] = IZQ
            estado["vx2"] = abs(estado["vx2"])
        elif estado["x2"] > DER:
            estado["x2"] = DER
            estado["vx2"] = -abs(estado["vx2"])

        if estado["y2"] < ARR:
            estado["y2"] = ARR
            estado["vy2"] = abs(estado["vy2"])
        elif estado["y2"] > ABA:
            estado["y2"] = ABA
            estado["vy2"] = -abs(estado["vy2"])

        #Colision entre bolas
        dx   = estado["x2"] - estado["x1"]
        dy   = estado["y2"] - estado["y1"]
        dist = (dx**2 + dy**2) ** 0.5

        if dist < 2*r and dist > 0:
            # Vector normal entre centros
            nx = dx / dist
            ny = dy / dist

            # Separar las bolas para que no se sobrepongan
            overlap = 2*r - dist
            estado["x1"] -= nx * overlap / 2
            estado["y1"] -= ny * overlap / 2
            estado["x2"] += nx * overlap / 2
            estado["y2"] += ny * overlap / 2

            # Velocidad relativa proyectada sobre el eje normal
            dvx = estado["vx1"] - estado["vx2"]
            dvy = estado["vy1"] - estado["vy2"]
            dot = dvx * nx + dvy * ny

            # Solo intercambiar si las bolas se están acercando
            if dot > 0:
                estado["vx1"] -= dot * nx
                estado["vy1"] -= dot * ny
                estado["vx2"] += dot * nx
                estado["vy2"] += dot * ny

        #Axtualizar la posicion en la que se ven las bolas
        canva_a.coords(bola1,
            estado["x1"]-r, estado["y1"]-r,
            estado["x1"]+r, estado["y1"]+r)
        canva_a.coords(bola2,
            estado["x2"]-r, estado["y2"]-r,
            estado["x2"]+r, estado["y2"]+r)

        # ── Siguiente frame solo si la ventana sigue abierta ────────
        if esta_abierta(ventana_ani):
            ventana_ani.after(16, actualizar)   # 16ms ≈ 60fps

    #Controles de velocidad de la animación
    panel = tk.Frame(ventana_ani, width=600, height=80, bg="lightgray")
    panel.pack(fill="x")
    panel.pack_propagate(False)  #evita que el frame se encoja

 #Indicador para reducir la velocidad
    velme = tk.Label(panel, text="-", bg="lightgray",font=("verdana", 14))
    velme.place(x=10, y=25)

    barravel = tk.Scale(panel, from_=0.1, to=4.0, resolution=0.1,
             orient="horizontal", variable=velocidad_var,
             length=380, bg="lightgray", font=("verdana", 9))
    barravel.place(x=40, y=5)

    velma = tk.Label(panel, text="+", bg="lightgray", font=("verdana", 14))
    velma.place(x=430, y=25)

    volver_a = tk.Button(panel, text="Volver al Menú", command=cerrar_ventana_ani,font=("verdana", 10))
    volver_a.place(x=480, y=25)

    #Texto de la ventana animacion
    labela = tk.Label(canva_a, text="Animación", bg="white", font=("verdana", 16, "bold"))
    labela.place(x=230, y=5)

    canva_a.create_rectangle(10, 40, 590, 420, outline="black", width=2)

    r = 25

    actualizar()



#Funcion para abrir la ventana de animación
def abrir_ventana_ani():
    if esta_abierta(ventana_ani):
        ventana_ani.lift()
    elif contador >= 1:      
        messagebox.showwarning("Límite", "Máximo 2 ventanas abiertas.")
    else:
        crear_ventana_ani()

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