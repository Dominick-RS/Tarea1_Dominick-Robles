import tkinter as tk
from tkinter import messagebox
import os
import pygame
pygame.mixer.init()

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
    ventana_Info.title("Ficha personal")
    ventana_Info.geometry("800x650")
    ventana_Info.resizable(False, False)
    ventana_Info.protocol("WM_DELETE_WINDOW", cerrar_ventana_Info)  #Manejo de ventanas
    contador += 1                               #Contador de ventana abierta

 #Canva de la ventana información y scrollbar
    canva_i = tk.Canvas(ventana_Info, width=780, height=660, bg="white")
    canva_i.pack(side="left", fill="both")
    scrollbar = tk.Scrollbar(ventana_Info, orient="vertical", command=canva_i.yview)
    canva_i.configure(yscrollcommand=scrollbar.set)      #Actualiza el canvas con el movimiento
    scrollbar.pack(side="right", fill="y")
    #Permite hacer scroll con los widgets del canvas
    frame_contenido = tk.Frame(canva_i, bg="white")
    canva_i.create_window((0, 0), window=frame_contenido, anchor="nw")

 #Cambia hasta donde se puede mover la ventana cada que se agrega un nuevo widget
    def actualizar_scroll(event):
        canva_i.configure(scrollregion=canva_i.bbox("all"))
    frame_contenido.bind("<Configure>", actualizar_scroll)

 #Titulo de ficha personal
    labeli = tk.Label(frame_contenido, text="Ficha Personal",
             bg="white", font=("verdana", 18, "bold"))
    labeli.pack(padx=300, pady=10)

 #Titulo datos personales
    data = tk.Label(frame_contenido, text="Datos Personales",
             bg="white", font=("verdana", 13, "bold"))
    data.pack(anchor="w", padx=20, pady=5)
 
 #Texto con el nombre
    nomb = tk.Label(frame_contenido, text="Nombre:   Dominick Robles Samudio",
             bg="white", font=("verdana", 11))
    nomb.pack(anchor="w", padx=40)
 
 #Texto con el carnet
    carnt = tk.Label(frame_contenido, text="Carnet:     2026093868",
             bg="white", font=("verdana", 11))
    carnt.pack(anchor="w", padx=40)
 
 #Texto con la edad
    edad = tk.Label(frame_contenido, text="Edad:       19 años",
             bg="white", font=("verdana", 11))
    edad.pack(anchor="w", padx=40, pady=(0,10))
 
 #Espacio para la biografía 
    bio = tk.Frame(frame_contenido, bg="gray", height=2, width=760)
    bio.pack(pady=5)

 #Titulo biografía
    biot = tk.Label(frame_contenido, text="Biografía",
             bg="white", font=("verdana", 13, "bold"))
    biot.pack(anchor="w", padx=20, pady=5)

    parrafb = tk.Label(frame_contenido,
             text="Mi nombre es Dominick, tengo 19 años, soy de Jaco y estoy estudiando ingeniería en computadores en el Tecnológico de Costa Rica.",
             bg="white", font=("verdana", 12),
             wraplength=720, justify="left")
    parrafb.pack(anchor="w", padx=30)  
 
 #Espacio para imagen del mapa
    mp = tk.Frame(frame_contenido, bg="gray", height=2, width=760)
    mp.pack(pady=5)

 #texto para el mapa
    tmp = tk.Label(frame_contenido, text="Lugar en donde vivo:",
             bg="white", font=("verdana", 13, "bold"))
    tmp.pack(anchor="w", padx=20, pady=5)
 
 #
    if os.path.exists("mapacasa.png"): #verifica el archivo
        mapa = tk.PhotoImage(file="mapacasa.png") #carga la imagen
        mapa = mapa.subsample(max(1, mapa.width() // 320), max(1, mapa.height() // 250)) #ajusta el tamaño
        lbl_mapa = tk.Label(frame_contenido, image=mapa, bg="white")  #widget de la imagen
        lbl_mapa.image = mapa  #evita que se elimine la imagen
        lbl_mapa.pack(pady=5)
 
 #label texto
    foto = tk.Label(frame_contenido, text="Fotografía:",
             bg="white", font=("verdana", 11, "bold"))
    foto.pack(anchor="w", padx=20) 

 #Se utiliza lo mismo que con lo anterior
    if os.path.exists("foto-perso.png"): 
        foto = tk.PhotoImage(file="foto-perso.png")  
        foto = foto.subsample(max(1, foto.width() // 180), max(1, foto.height() // 280))  
        lbl_foto = tk.Label(frame_contenido, image=foto, bg="white")
        lbl_foto.image = foto
        lbl_foto.pack(pady=5)

    conte = tk.Frame(frame_contenido, bg="gray", height=2, width=760)
    conte.pack(pady=5)

    artt = tk.Label(frame_contenido, text="Artista Favorito",
             bg="white", font=("verdana", 13, "bold"))
    artt.pack(anchor="w", padx=20, pady=5)

    artn = tk.Label(frame_contenido, text="Nombre:   Alvaro Díaz",
             bg="white", font=("verdana", 11))
    artn.pack(anchor="w", padx=40)
 
    artg = tk.Label(frame_contenido, text="Género:    Reguetón",
             bg="white", font=("verdana", 11))
    artg.pack(anchor="w", padx=40, pady=(0,10))

    if os.path.exists("foto_artista.png"):
        foto_art = tk.PhotoImage(file="foto_artista.png")
        foto_art = foto_art.subsample(max(1, foto_art.width() // 250), max(1, foto_art.height() // 250))  
        lbl_art = tk.Label(frame_contenido, image=foto_art, bg="white")
        lbl_art.image = foto_art
        lbl_art.pack(pady=5)
 
 #Espacio para el texto de la canción
    music =tk.Frame(frame_contenido, bg="gray", height=2, width=760)
    music.pack(pady=5)

   #Texto canción 
    texmus = tk.Label(frame_contenido, text="Canción (10 segundos):",
             bg="white", font=("verdana", 13, "bold"))
    texmus.pack(anchor="w", padx=20, pady=5)

 #Espacio canción y botones
    frame_audio = tk.Frame(frame_contenido, bg="white")
    frame_audio.pack(pady=5)

    #Funcion para iniciar a reproducir la canción
    def reproducir():
        if os.path.exists("cancion.mp3"):   
            pygame.mixer.music.load("cancion.mp3") #carga el archivo
            pygame.mixer.music.play()   #reproduce el audio
    
    #Funcion para detener la canción
    def detener():
        pygame.mixer.music.stop()

    tk.Button(frame_audio, text="▶ Reproducir", command=reproducir,
              font=("verdana", 11), bg="green", fg="white", width=12).pack(side="left", padx=10)
    tk.Button(frame_audio, text="⏹ Detener", command=detener,
              font=("verdana", 11), bg="red", fg="white", width=12).pack(side="left", padx=10)
   
    

    volveri = tk.Frame(frame_contenido, bg="gray", height=2, width=760)
    volveri.pack(pady=10)
    volverim = tk.Button(frame_contenido, text="Volver al Menú",
              command=cerrar_ventana_Info,
              font=("verdana", 11))
    volverim.pack(pady=10)

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

    # Estado de las dos bolas, posición y velocidad
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

        #Mueve las bolas según velocidad actual de la barra
        estado["x1"] += estado["vx1"] * speed  #
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

        #Calcula si sucede la colision entre bolas
        dx   = estado["x2"] - estado["x1"]
        dy   = estado["y2"] - estado["y1"]
        dist = (dx**2 + dy**2) ** 0.5

            #Calcula el intercambio de velocidades en el choque
        if dist < 2*r and dist > 0:
            nx = dx / dist          #Vector normal entre centros
            ny = dy / dist

            # Separar las bolas para que no se sobrepongan
            overlap = 2*r - dist
            estado["x1"] -= nx * overlap / 2
            estado["y1"] -= ny * overlap / 2
            estado["x2"] += nx * overlap / 2
            estado["y2"] += ny * overlap / 2

            # Velocidad relativa proyectada sobre el eje normal
            dvx = estado["vx1"] - estado["vx2"]
            dvy = estado["vy1"] - estado["vy2"] #Velocidad entre las 2 bolas
            dot = dvx * nx + dvy * ny

            #La fisica del choque
            if dot > 0:                   #inidica que las bolas se están acercando, entonces intercambia las velocidades en ese eje
                estado["vx1"] -= dot * nx
                estado["vy1"] -= dot * ny
                estado["vx2"] += dot * nx
                estado["vy2"] += dot * ny

        #Actualizar la posicion en la que se ven las bolas
        canva_a.coords(bola1,
            estado["x1"]-r, estado["y1"]-r,
            estado["x1"]+r, estado["y1"]+r)
        canva_a.coords(bola2,
            estado["x2"]-r, estado["y2"]-r,
            estado["x2"]+r, estado["y2"]+r)

        #Actualiza cada 16 milisegundos
        if esta_abierta(ventana_ani):
            ventana_ani.after(16, actualizar)   #Indica a tkinter actualizar cada 16 ms

    #Controles de velocidad de la animación
    panel = tk.Frame(ventana_ani, width=600, height=80, bg="lightgray")
    panel.pack(fill="x")
    panel.pack_propagate(False)  #evita que el frame se encoja

 #Barra para cambiar la velocidad
    barravel = tk.Scale(panel, from_=0.1, to=4.0, resolution=0.1,
             orient="horizontal", variable=velocidad_var,
             length=380, bg="lightgray", font=("verdana", 9))
    barravel.place(x=40, y=5)

    #Indicador para reducir la velocidad
    velme = tk.Label(panel, text="-", bg="lightgray",font=("verdana", 14))
    velme.place(x=10, y=25)

 #Indicador para aumentar la velocidad de la animación
    velma = tk.Label(panel, text="+", bg="lightgray", font=("verdana", 14))
    velma.place(x=430, y=25)
 
 #Boton para volver al menú
    volver_a = tk.Button(panel, text="Volver al Menú", command=cerrar_ventana_ani,font=("verdana", 10))
    volver_a.place(x=480, y=25)

    #Texto de la ventana animacion
    labela = tk.Label(canva_a, text="Animación", bg="white", font=("verdana", 16, "bold"))
    labela.place(x=230, y=5)

    #Rectangulo dentro del que sucede la animación y se nota su limite
    canva_a.create_rectangle(10, 40, 590, 420, outline="black", width=2)

 #Ejecuta la animación
    actualizar()



#Funcion para abrir la ventana de animación
def abrir_ventana_ani():
    if esta_abierta(ventana_ani):
        ventana_ani.lift()
    elif contador >= 1:      
        messagebox.showwarning("Límite", "Máximo 2 ventanas abiertas.")
    else:
        crear_ventana_ani()

#Funcion para cerrar la ventana de animación
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