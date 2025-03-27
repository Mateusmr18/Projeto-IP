
import pygame
from pygame import  draw
from pygame.math import Vector2


class Protagonista():
    def __init__(self, imagem, x_inicial, y_inicial, velocidade):
        self.imagem = imagem
        self.x = x_inicial
        self.y= y_inicial
        self.velocidade = velocidade

    def mover(self, movimento):
        if movimento == pygame.K_LEFT: 
            self.x -= self.velocidade
        elif movimento == pygame.K_RIGHT: 
            self.x += self.velocidade
        elif movimento == pygame.K_UP: 
            self.y -= self.velocidade
        elif movimento == pygame.K_DOWN: 
            self.y += self.velocidade

    def desenhar(self, tela):
            draw.rect(tela, "red", (self.x, self.y, 24, 24))
    
    def local(self):
        return Vector2(self.x, self.y)

