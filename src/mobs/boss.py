import pygame
from pygame import image, transform

class BossKurt(pygame.sprite.Sprite):
    def __init__(self, posicao_inicial, velocidade):
        pygame.sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load("assets/kurt.png"), (velocidade, velocidade))
        self.rect = self.image.get_rect()
        self.rect.topleft  = posicao_inicial
        self.velocidade = velocidade
        self.posicao = self.rect.topleft


    



