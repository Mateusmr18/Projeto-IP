
import pygame
from pygame import  draw
from pygame.math import Vector2


class Protagonista(pygame.sprite.Sprite):
    def __init__(self, nome ,imagem, posicao_inicial, obj_vida, mob_manager):
        pygame.sprite.Sprite.__init__(self)
        self.nome = nome
        self.image = pygame.Surface((50, 50))
        self.image.fill("red")

        self.rect = self.image.get_rect()
        self.rect.bottomleft  = posicao_inicial
        
        self.velocidade = 10

        self.esta_pulando = False
        self.contador_pulo = 10

        self.vida = obj_vida

        self.mob_manager = mob_manager

        self.posicao = "cima"


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

    def attack(self):
        self.mob_manager.shoot("normal", self.nome , self.rect.center, (0, -1), 10, 1)
    
    def get_hit(self, dano):
        self.vida.reduzir_vida(dano)

    def get_posicao(self):
        return Vector2(self.rect.center)
    
    def get_nome(self):
        return self.nome

