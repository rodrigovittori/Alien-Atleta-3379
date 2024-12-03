#pgzero

"""
# [M5.L3] - Actividad #5: "Puntuación"
# Objetivo: Implementar un sistema de puntuación que registre la cant. de enemigos esquivados

Nota: La actividad # 4 ya estaba resuelta por el código de nuestra actividad #3

1º Creamos una variable que almacene nuestra puntuación
2º Modifico el draw() para que muestre la puntuación
3º Modifico el reset para que reinicie nuestra puntuación
4º Aumentaremos la puntuación cada vez que un enemigo haya abandonado la pantalla


Nota: distancia spawn abeja aumentada a WIDTH + 350; box.y cambiado 265, velocidad del personaje a 7
-> agregar aumento de velocidad de los enemigos al resetearse

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
caja  = Actor("box", (WIDTH-50, 265)) 
abeja = Actor("bee", (WIDTH + 350, 150))

# Variables
anim = 1 # variable temporal para demostrar las animaciones
COOLDOWN_SALTO = 0.6 # tiempo de recarga habilidad salto (en segundos)
timer_salto = 0 # tiempo que debe pasar (en segundos) antes de que nuestro personaje pueda saltar nuevamente
nva_imagen = "alien" # "alien": quieto / "left": mov. izq. / "right" : mov. dcha.
game_over = False
puntuacion = 0 # Cantidad de enemigos esquivados

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

    if (game_over):
        fondo.draw()
        cartel_game_over.draw()
        # Nota: modificamos la altura del otro mensaje para mostrar más info:
        screen.draw.text(("Enemigos esquivados: " + str(puntuacion)), center= (int(WIDTH/2), 2* int(HEIGHT/3)), color = "yellow", fontsize = 24)
        screen.draw.text("Presiona [Enter] para reiniciar", center= (int(WIDTH/2), 4* int(HEIGHT/5)), color = "white", fontsize = 32)

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

    global timer_salto, nva_imagen, game_over, puntuacion

    if (game_over):
        # En caso de game_over
        if (keyboard.enter):
        
            ########################
            # GAME OVER - RESETEAR #
            ########################
    
            # To-do: Migrar a funcion
            
            game_over = False
            puntuacion = 0
            personaje.pos = (50, 240)
            personaje.esta_agachado = False
            nva_imagen = 'alien'
            timer_salto = 0
            caja.pos = (WIDTH + 50, 265)
            caja.angle = 0
            abeja.pos = (WIDTH + 350, 150)

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
        
        # Actualizamos la caja - Migrar a función
    
        # Rotación
        if caja.angle < 360:
            caja.angle = caja.angle + 5
        else:
            caja.angle = caja.angle - 360 + 5
    
        # Posición
        if (caja.x < (int(caja.width/2))):
            puntuacion += 1
            caja.x += WIDTH
        else:
            caja.x -= 5 # mover la caja 5 px a la izquierda en cada frame
    
        # Actualizamos la abeja - Migrar a función
    
        # To-Do: agregar "zig-zagueo" de la abeja
    
        # Posición
        if (abeja.x < (int(abeja.width/2))):
            puntuacion += 1
            abeja.x += WIDTH
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
                game_over = True
        
        
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