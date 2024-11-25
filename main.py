#pgzero

"""
# M5.L3 - Actividad #3: "Controles"
# Objetivo: Controlar el movimiento del personaje con el teclado

# NOTA: El ejercicio M5.L2 NO forma parte de la cadena de soluciones
#       por cambio de assets y para evitar confusiones.

# Paso Nº 1) Agregar un if con DOS condiciones:
            -> Condicion #1: Que el usuario presione la tecla deseada
                             (A o flecha izq.) // (D o flecha derecha)

# NOTA: Ajustamos la altura de la caja a 260
"""

WIDTH = 600 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana

TITLE = "Juego del Alien Atleta y sus piruetas" # Título para la ventana del juego
FPS = 30 # Número de fotogramas por segundo

#crea un personaje aquí
personaje = Actor("alien", (50, 240))
personaje.velocidad = 5 # velocidad (en px) a la que avanza el personaje por cada frame

""" Nota: Si quisieramos facilitar la tarea de "reiniciar"/"resetear"
          la posición del personaje o los obstáculos/enemigos a su estado
          inicial, podemos hacerlo de la siguiente manera:

    Paso 1) Creamos un atributo del actor donde registramos su posición inicial:

personaje.posInicial = personaje.pos # almacenamos la posición inicial

    Paso 2) Cuando querramos resetear la posición, usaremos:

personaje.pos = personaje.posInicial
"""

fondo = Actor("background")
caja = Actor("box", (WIDTH-50, 260)) 

def draw():
    fondo.draw()
    personaje.draw()
    caja.draw()
    
def update(dt): # Podemos traducir "update" como "actualizar", es decir, en ella contendremos el código que produzca cambios en nuestro juego
    
    # Actualizamos el personaje

    if (keyboard.right or keyboard.d) and (personaje.x < WIDTH - int(personaje.width/2)):
        personaje.x += personaje.velocidad

    if (keyboard.left or keyboard.a) and (personaje.x > int(personaje.width/2)):
        personaje.x -= personaje.velocidad

    ########################
    
    # Actualizamos la caja

    # Rotación
    if caja.angle < 360:
        caja.angle = caja.angle + 5
    else:
        caja.angle = caja.angle - 360 + 5

    # Posición
    if (caja.x < (int(caja.width/2))):
        caja.x += WIDTH
    else:
        caja.x -= 5 # mover la caja 5 px a la izquierda en cada frame

    # para cerrar el juego
    if keyboard.q:
        exit()