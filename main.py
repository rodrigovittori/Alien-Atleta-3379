#pgzero

"""
# [M5.L3] - Actividad #2: "Colisión con una abeja"
# Objetivo: Agregar lógica de colisión para la abeja

NOTA: En el programa han eliminado la actividad donde creábamos la abeja, así que toca crearla en éste ejercicio.

1º Crear actor abeja
2º La agregamos en nuestro draw()
3º Agregamos los controles de movimiento automático para la abeja
    Nota: agregarlos 50 y 150 al "reset" de posición de la caja y la abeja
4º Agregamos la condición de colliderect() con un "or"

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
personaje.timer_agachado = 0.0 # Tiempo restante (en segundos) antes de poner de pie al personaje
personaje.esta_agachado = False


# Otros Actores:

fondo = Actor("background")
caja  = Actor("box", (WIDTH-50, 260)) 
abeja = Actor("bee", (WIDTH + 150, 150))

# Variables
anim = 1 # variable temporal para demostrar las animaciones
COOLDOWN_SALTO = 0.6 # tiempo de recarga habilidad salto (en segundos)
timer_salto = 0 # tiempo que debe pasar (en segundos) antes de que nuestro personaje pueda saltar nuevamente
nva_imagen = "alien" # "alien": quieto / "left": mov. izq. / "right" : mov. dcha.

def animar(op):
    if op == 1:
        animate(personaje, tween="linear", duration=2, x = WIDTH-35, y = HEIGHT-45)
    elif (op == 2):
        animate(personaje, tween="bounce_start_end", duration=2, x = 35, y = 45)
    elif (op == 3):
        animate(personaje, tween="accel_decel", duration = 2, x= WIDTH - 35, y = HEIGHT-45)
    else:
        animate(personaje, tween="bounce_start_end", duration = 2, x= 35, y = HEIGHT-45)



def draw():
    fondo.draw()
    personaje.draw()
    caja.draw()
    abeja.draw()

    if (timer_salto <= 0):
        screen.draw.text("¡LISTO!", midleft=(20,20), color = (0, 255, 0), fontsize=24)
    else:
        screen.draw.text(str(timer_salto), midleft=(20,20), color = "red", fontsize=24)    

    
def update(dt): # Podemos traducir "update" como "actualizar", es decir, en ella contendremos el código que produzca cambios en nuestro juego

    global timer_salto, nva_imagen

    #######################
    # CAMBIOS AUTOMATICOS #
    #######################

    timer_salto -= dt
    nva_imagen = "alien" # Si el personaje NO se mueve, mostraremos esta imágen
    personaje.timer_agachado -= dt

    if ((personaje.timer_agachado <= 0) and (personaje.esta_agachado)): 
        personaje.y = 240
        personaje.esta_agachado = False
    
    ########################
    
    # Actualizamos la caja - Migrar a función

    # Rotación
    if caja.angle < 360:
        caja.angle = caja.angle + 5
    else:
        caja.angle = caja.angle - 360 + 5

    # Posición
    if (caja.x < (int(caja.width/2))):
        caja.x += WIDTH + 50
    else:
        caja.x -= 5 # mover la caja 5 px a la izquierda en cada frame

    # Actualizamos la abeja - Migrar a función

    # To-Do: agregar "zig-zagueo" de la abeja

    # Posición
    if (abeja.x < (int(abeja.width/2))):
        abeja.x += WIDTH + 150
    else:
        abeja.x -= 5 # mover la caja 5 px a la izquierda en cada frame

    ################
    # LEER TECLADO #
    ################
    
    # Movimiento del personaje

    if (keyboard.right or keyboard.d) and (personaje.x < WIDTH - int(personaje.width/2)):
        personaje.x += personaje.velocidad
        nva_imagen = "right"

    if (keyboard.left or keyboard.a) and (personaje.x > int(personaje.width/2)):
        personaje.x -= personaje.velocidad
        nva_imagen = "left"

    if (keyboard.down or keyboard.s):
        personaje.y = 260
        nva_imagen = "duck"
        personaje.timer_agachado = 0.1
        personaje.esta_agachado = True

    ##############
    # COLISIONES #
    ##############

    # To-Do: migrar a función

    if (personaje.colliderect(caja) or personaje.colliderect(abeja)):
        if (nva_imagen != "hurt"):
            nva_imagen = "hurt"
    
    
    ### POST INPUT ###

    personaje.image = nva_imagen # Actualizamos el sprite del personaje

#####################

def on_key_down(key): # Esta función se activa al presionar una tecla
    # https://pygame-zero.readthedocs.io/en/stable/hooks.html?highlight=on_key_down#on_key_down
    
    global anim, timer_salto
    
    """
    if (keyboard.space): #Si pulso la barra espaciadora
        animar(anim)     # Activo la animación actual
        anim += 1
        # actualizo el número de animación actual
        if anim >= 5:
            anim = 1
    """

    if (keyboard.space or keyboard.w or keyboard.up) and (timer_salto <= 0) and (personaje.y > int(personaje.height / 2)):
        timer_salto = COOLDOWN_SALTO
        personaje.y -= personaje.height
        animate(personaje, tween="bounce_end", duration = 2, y=240)
    
    # para cerrar el juego
    if (keyboard.q):
        exit()