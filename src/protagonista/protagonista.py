
import pygame
from pygame import  draw
from pygame.math import Vector2


class Protagonista(pygame.sprite.Sprite):
    def __init__(self, imagem, posicao_inicial, velocidade, obj_vida):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48, 48))
        self.image.fill("red")

        self.rect = self.image.get_rect()
        self.rect.bottomleft  = posicao_inicial
        
        self.posicao = posicao_inicial
        
        self.velocidade = velocidade

        self.esta_pulando = False
        self.contador_pulo = 10

        self.vida = obj_vida


    def carregar_mapa(self, mapa):
        self.mapa = mapa

    def mover(self, entrada):
        movimento = (0,0)
        if entrada[pygame.K_LEFT]:
            movimento = (-self.velocidade, 0)
        elif entrada[pygame.K_RIGHT]: 
            movimento = (+self.velocidade, 0)
        
        
        
        if entrada[pygame.K_UP] or self.esta_pulando:
            movimento += Vector2(self.pular())

        nova_posicao= Vector2(self.rect.bottomleft) + movimento

        if self.mapa.pode_andar(nova_posicao):
            self.rect.bottomleft = nova_posicao

    

    def pular(self):

        self.esta_pulando = True

        y = 0

        if self.contador_pulo >= -10:
            y = (self.contador_pulo * abs(self.contador_pulo)) * 0.5
            self.contador_pulo -=1
        else:
            self.contador_pulo = 10
            self.esta_pulando = False


        return (0, -y)


    

