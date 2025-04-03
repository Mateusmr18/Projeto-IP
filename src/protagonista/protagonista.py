
import pygame
from pygame import  draw
from pygame.math import Vector2


class Protagonista(pygame.sprite.Sprite):
    def __init__(self, imagem, posicao_inicial, velocidade = 48):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((48, 48))
        self.image.fill("red")

        self.rect = self.image.get_rect()
        self.rect.topleft  = posicao_inicial

        
        self.posicao = self.rect.topleft
        self.velocidade = velocidade


    def carregar_mapa(self, mapa):
        self.mapa = mapa

    def mover(self, entrada):
        if entrada == pygame.K_LEFT: 
            movimento = (-self.velocidade, 0)
        elif entrada == pygame.K_RIGHT: 
            movimento = (+self.velocidade, 0)
        elif entrada == pygame.K_UP: 
            movimento = (0, -self.velocidade)
        elif entrada == pygame.K_DOWN: 
            movimento = (0, +self.velocidade)


        nova_posicao= Vector2(self.rect.topleft) + movimento

        if self.mapa.pode_andar(nova_posicao):
            self.rect.topleft = nova_posicao
    
        print(self.rect.topleft)

    def pegar_posicao(self):
        return self.rect.topleft
    
    

