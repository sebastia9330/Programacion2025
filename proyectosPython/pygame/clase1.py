import pygame
import constantes
from personaje import Personaje


def escalar_img(imagen, scala):
    w = imagen.get_width()
    h = imagen.get_height()
    nueva_imagen = pygame.transform.scale(imagen, (w*scala, h*scala))
    return nueva_imagen

animaciones = []
for i in range(8):
    img = pygame.image.load(f"C:\\OD\\OneDrive - TI\\Documentos\\Sebastian Carrero\\Programacion2025\\proyectosPython\\pygame\\assets\\imagenes\\caracteres\\personaje\\frame_{i}.png")
    img = escalar_img(img, constantes.SCALA_PERSONAJE)
    animaciones.append(img)


jugador = Personaje(50, 50, animaciones)

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))

pygame.display.set_caption("Mi primer juego")


#definir variables de movimiento del jugador

mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

#controlar el frame_rate
reloj = pygame.time.Clock()

run = True

while run:

    #FPS = 60
    reloj.tick(constantes.FPS)

    ventana.fill(constantes.COLOR_BG)

    jugador.dibujar(ventana)

    #calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD

    #mover al jugador
    jugador.movimiento(delta_x, delta_y)

    jugador.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda =False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False

    print(f"{delta_x}, {delta_y}")
    pygame.display.update()

pygame.quit()