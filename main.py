#pgzero

"""
# M5.L2 - Actividad #1: "Actualizando la caja"
# Objetivo: lograr que los obstáculos reaparezcan tras abandonar la ventana

1º Agregar condicion (if) para la que cuando la caja (o el personaje)
    se salga de la pantalla (WIDTH), vuelva a su posición inicial
"""

WIDTH = 600 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana

TITLE = "Juego del Alien Atleta y sus piruetas" # Título para la ventana del juego
FPS = 30 # Número de fotogramas por segundo

#crea un personaje aquí
personaje = Actor("alien", (50, 240))

""" Nota: Si quisieramos facilitar la tarea de "reiniciar"/"resetear"
          la posición del personaje o los obstáculos/enemigos a su estado
          inicial, podemos hacerlo de la siguiente manera:

    Paso 1) Creamos un atributo del actor donde registramos su posición inicial:

personaje.posInicial = personaje.pos # almacenamos la posición inicial

    Paso 2) Cuando querramos resetear la posición, usaremos:

personaje.pos = personaje.posInicial
"""

fondo = Actor("background")
caja = Actor("box", (WIDTH-50, 240))

def draw():
    fondo.draw()
    personaje.draw()
    caja.draw()
    
def update(dt): # Podemos traducir "update" como "actualizar", es decir, en ella contendremos el código que produzca cambios en nuestro juego
    
    # Actualizamos el personaje

    if (personaje.x > (WIDTH - int(personaje.width /2))):
        personaje.x -= WIDTH
    else:
         personaje.x += 5 #Lo muevo a la derecha

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