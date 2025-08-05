import pygame
import constantes

class Personaje():
    def __init__(self, x, y):
        self.shape = pygame.Rect(0,0,constantes.ANCHO_PERSONAJE,constantes.ALTO_PERSONAJE)
        self.shape.center = (x,y)

    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, self.shape)