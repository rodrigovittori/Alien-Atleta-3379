#pgzero
import random

"""
# [M5.L4 - Actividad #3: "Enemigos aleatorios"]
# Objetivo: Llamar al próximo obstáculo/enemigo según un valor random

Modificamos el sistema de obstáculos para actualizar uno a la vez, que se determina de forma aleatoria

Pasos:
1º Importar el módulo random
2º Crear la vble "prox_enemigo", que tomará un valor random entre 1 y 2
   (xq sólo tenemos dos tipos de enemigos)
3º Creamos una función que calcule el valor de nuestro próximo enemigo en forma aleatoria
4º En update(dt) llamaremos a la función que actualiza el obstáculo/enemigo "activo",
    hasta que salga de la pantalla, (luego reasignaremos ese valor random)
5º Agregar a la función reiniciar_juego una condición para reestablecer el valor del prox_enemigo a spwanear

Nota: Para evitar ver la caja cuando no se está moviendo modificamos su posición al inicializarla, resetearla y moverla

"""

WIDTH = 600 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana

TITLE = "Juego del Alien Atleta y sus piruetas" # Título para la ventana del juego
FPS = 30 # Número de fotogramas por segundo

#crea un personaje aquí
personaje = Actor("alien", (50, 240))
personaje.velocidad = 7 # velocidad (en px) a la que avanza el personaje por cada frame

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
cartel_game_over = Actor("GO")
caja  = Actor("box", (WIDTH + 50, 265)) 
abeja = Actor("bee", (WIDTH + 350, 150))

# Variables
anim = 1 # variable temporal para demostrar las animaciones
COOLDOWN_SALTO = 0.6 # tiempo de recarga habilidad salto (en segundos)
timer_salto = 0 # tiempo que debe pasar (en segundos) antes de que nuestro personaje pueda saltar nuevamente
nva_imagen = "alien" # "alien": quieto / "left": mov. izq. / "right" : mov. dcha. / "hurt": tomó daño
game_over = False
texto_colision = " "
puntuacion = 0 # Cantidad de enemigos esquivados
prox_enemigo = random.randint(1,2) # 1: Caja / 2: Abeja

"""  #####################
    # FUNCIONES PROPIAS #
   #####################  """

def animar(op):
    if op == 1:
        animate(personaje, tween="linear", duration=2, x = WIDTH-35, y = HEIGHT-45)
    elif (op == 2):
        animate(personaje, tween="bounce_start_end", duration=2, x = 35, y = 45)
    elif (op == 3):
        animate(personaje, tween="accel_decel", duration = 2, x= WIDTH - 35, y = HEIGHT-45)
    else:
        animate(personaje, tween="bounce_start_end", duration = 2, x= 35, y = HEIGHT-45)

def enemigo_al_azar():
    """
    Numero entero de 1 a (cant_enemigos)
    1: Caja
    2: Abeja
    """
    return random.randint(1, 2) # Nota: actualizar cuando se agreguen tipos de enemigos


def actualizar_abeja():
    global puntuacion, prox_enemigo

    # To-Do: agregar "zig-zagueo" de la abeja
    
    # Posición
    if (abeja.x < (-int(abeja.width))):
        puntuacion += 1
        abeja.x = WIDTH + 150
        prox_enemigo = enemigo_al_azar()
        
    else:
        abeja.x -= 5 # mover la caja 5 px a la izquierda en cada frame
        # Nota: Posibilidad de que los enemigos aceleren cada vez que respawnean
        #       -> x.- vble global: velocidad_enemigos

def actualizar_caja():
    global puntuacion, prox_enemigo

    # To-Do: agregar "zig-zagueo" de la abeja
    
    # Rotación
    if caja.angle < 360:
        caja.angle = caja.angle + 5
    else:
        caja.angle = caja.angle - 360 + 5
    
    # Posición
    if (caja.x < (int(caja.width/2))):
        puntuacion += 1
        caja.x = WIDTH + 50
        prox_enemigo = enemigo_al_azar()
    else:
        caja.x -= 5 # mover la caja 5 px a la izquierda en cada frame
        # Nota: Posibilidad de que los enemigos aceleren cada vez que respawnean
        #       -> x.- vble global: velocidad_enemigos


def actualizar_texto_colision(tipo_colision):

    texto_colision = " "
    
    if (tipo_colision == 1): # CAJA
        texto_colision = "¡Entrega letal!"

    elif (tipo_colision == 2): # ABEJA
        texto_colision = "¡Eres alérgico a las abejas!"

    return texto_colision

def detectar_colisiones():
    global nva_imagen, game_over, texto_colision
    
    if personaje.colliderect(caja):
        texto_colision = actualizar_texto_colision(1)
        if (nva_imagen != "hurt"):
            nva_imagen = "hurt"
        game_over = True
            
    elif personaje.colliderect(abeja):
        texto_colision = actualizar_texto_colision(2)
        if (nva_imagen != "hurt"):
            nva_imagen = "hurt"
        game_over = True

def mover_personaje():
    global nva_imagen, timer_salto
 
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

def reiniciar_juego():
    global game_over, puntuacion, nva_imagen, timer_salto, texto_colision, prox_enemigo
    
    game_over = False
    puntuacion = 0
    personaje.pos = (50, 240)
    personaje.esta_agachado = False
    personaje.timer_agachado = 0.0
    nva_imagen = 'alien'
    timer_salto = 0
    caja.pos = (WIDTH + 50, 265)
    caja.angle = 0
    abeja.pos = (WIDTH + 350, 150)
    texto_colision = " "
    prox_enemigo = enemigo_al_azar()

"""  ####################
    # FUNCIONES PGZERO #
   ####################  """

def draw():

    if (game_over):
        fondo.draw()
        cartel_game_over.draw()
        # Nota: modificamos la altura del otro mensaje para mostrar más info:
        screen.draw.text(("Enemigos esquivados: " + str(puntuacion)), center= (int(WIDTH/2), 2* int(HEIGHT/3)), color = "yellow", fontsize = 24)
        screen.draw.text("Presiona [Enter] para reiniciar", center= (int(WIDTH/2), 4* int(HEIGHT/5)), color = "white", fontsize = 32)
        
        screen.draw.text(texto_colision, center= (int(WIDTH/2), int(HEIGHT/5)), color = "red", fontsize = 24)

    else:
        fondo.draw()
        personaje.draw()
        caja.draw()
        abeja.draw()
    
        if (timer_salto <= 0):
            screen.draw.text("¡LISTO!", midleft=(20,20), color = (0, 255, 0), fontsize=24)
        else:
            screen.draw.text(str(timer_salto), midleft=(20,20), color = "red", fontsize=24)    

        screen.draw.text(("Enemigos esquivados: " + str(puntuacion)), midright=(WIDTH-20, 20), color ="black", background="white", fontsize=24)

    
    
def update(dt): # Podemos traducir "update" como "actualizar", es decir, en ella contendremos el código que produzca cambios en nuestro juego

    global timer_salto, nva_imagen

    if (game_over):
        # En caso de game_over
        if (keyboard.enter):
            reiniciar_juego()

    else:
        # Si NO es game_over...
        
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

        # Actualizamos los enemigos
        # Nota: creo que ésto después lo migramos a otra función
        if (prox_enemigo == 1):
            actualizar_caja()
        elif (prox_enemigo == 2):
            actualizar_abeja()
            # Nota: actualizar cuando se agreguen tipos de enemigos
   
        mover_personaje()
    
        detectar_colisiones()
        
        
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