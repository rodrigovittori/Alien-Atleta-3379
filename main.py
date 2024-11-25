# [M5.L2] - Actividad #0: Copiamos tarea pasada

#pgzero

WIDTH = 600 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana

TITLE = "Juego del Alien Atleta y sus piruetas" # Título para la ventana del juego
FPS = 30 # Número de fotogramas por segundo

#crea un personaje aquí
personaje = Actor("alien", (50, 240))
fondo = Actor("background")
caja = Actor("box", (WIDTH-50, 240))

def draw():
    fondo.draw()
    personaje.draw()
    caja.draw()
    
def update(dt):
    personaje.x += 5
    caja.x -= 5
    
    personaje.angle -= 5

    if caja.angle < 360:
        caja.angle = caja.angle + 5
    else:
        caja.angle = caja.angle - 360 + 5

    if keyboard.q:
        exit()