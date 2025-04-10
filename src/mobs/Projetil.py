import pygame
from pygame import Surface, Vector2
import math
import random

class Projetil(pygame.sprite.Sprite):
    def __init__(self, dono, posicao, vetor_direcao = (0,0), velocidade = 10, dano = 1):
        super().__init__()
        self.dono = dono
        self.image = Surface((24, 24))
        self.image.fill("blue")
        self.rect = self.image.get_rect(center = posicao)
        self.velocidade = velocidade * Vector2(vetor_direcao)
        self.dano = dano

    
    def update(self):
        posicao = Vector2(self.rect.center)
        self.rect.center = posicao + self.velocidade


    def get_dano(self):
        return self.dano
    
    def get_dono(self):
        return self.dono
    
    def saiu_tela(self):
        x, y = Vector2(self.rect.center)
        if (x < 0 or x> 800 or y < 0 or y > 600):
            return True
        return False
    

class NotaVibra(pygame.sprite.Sprite):
    def __init__(self, dono, posicao, velocidade = 3, dano = 1, chegada = (0,0)):
        super().__init__()
        self.dono = dono

        self.image = Surface((24, 24))
        self.image.fill("yellow")
        self.rect = self.image.get_rect(center = posicao)
        self.velocidade = velocidade
        self.dano = dano

        self.frequencia_onda = 0.05  # Frequência da onda (quanto maior, mais rápida a onda)
        self.amplitude_onda = 7 # Amplitude da onda (quanto maior, maior o desvio)
        self.chegada = Vector2(chegada)
        self.frame_count = 0
        self.direcao = (self.chegada - Vector2(posicao)).normalize()
        self.angulo = Vector2(chegada).angle_to(self.rect.center)


    def update(self):
        self.frame_count+=1
        self.rect.center = self.gira_projetio()


    def gira_projetio(self):
        movimento_x = self.direcao.x * self.velocidade

        movimento_y = self.direcao.y * self.velocidade + self.amplitude_onda * math.cos(self.frame_count * self.frequencia_onda)

        nova_posicao = Vector2(self.rect.center) + Vector2(movimento_x, movimento_y)

        return nova_posicao

    def get_dano(self):
        return self.dano
    

    def get_dono(self):
        return self.dono
    
    def saiu_tela(self):
        x, y = Vector2(self.rect.center)
        if (x < 0 or x> 1600 or y < 0 or y > 1200):
            return True
        return False
    
class LittleShots(Projetil):
    def __init__(self, dono, posicao, vetor_direcao = (0,0), velocidade = 10, dano = 1):
        super().__init__(dono, posicao, vetor_direcao, velocidade, dano)
        self.image.fill("purple")


class NotaDivide(pygame.sprite.Sprite):
    def __init__(self, dono, posicao, mob_manager, velocidade = 3, dano = 1, ):
        super().__init__()
        self.dono = dono

        self.image = Surface((24, 24))
        self.image.fill("black")
        self.rect = self.image.get_rect(center = posicao)
        self.velocidade = velocidade
        self.dano = dano
        self.localizacao = Vector2(1,0).rotate((random.uniform(0, 180)))
        self.ticks = random.uniform(50, 200)
        self.mob_manager = mob_manager

    def update(self):
        self.rect.center+= self.localizacao * self.velocidade
        self.ticks-=1
        self.dividir()

    def dividir(self):

        if self.ticks <= 0:
            lista = [Vector2(1, 0).rotate((360 / 5) * i) for i in range(5)]
            for i in range(5):
                self.mob_manager.shoot("pequenina", self.dono, self.rect.center, lista[i], self.velocidade * 2, dano=1)


        

    def get_dano(self):
        return self.dano
    
    def get_dono(self):
        return self.dono

    
    def saiu_tela(self):
        x, y = Vector2(self.rect.center)
        if (x < 0 or x> 1600 or y < 0 or y > 1200):
            return True
        
        if self.ticks <= 0:
            return True
        return False


class Batidao(pygame.sprite.Sprite):
    def __init__(self, dono, velocidade_crescimento = 1, dano = 1):
        super().__init__()
        self.dono = dono
        self.tamanho = 1
        self.tamanho_maximo = 60
        self.image = Surface((1, 1))
        self.posicao = (random.uniform(20, 780), random.uniform(300, 600))
        self.rect = self.image.get_rect(center = self.posicao)
        self.velocidade_crescer = velocidade_crescimento * 60
        self.dano = dano
        self.frames = 0


    def update(self):
        tela_nova = Surface((self.tamanho+2, self.tamanho+2), pygame.SRCALPHA)
        pygame.draw.circle(tela_nova, "yellow", (Vector2(tela_nova.get_size()) / 2), self.tamanho / 2, 2)

        self.image = tela_nova
        self.rect = self.image.get_rect(center = self.posicao)
        
        if self.frames > 3:
            self.frames = 0
            self.tamanho+=1

        self.frames+=1

        
    def get_dano(self):
        return self.dano
    
    def get_dono(self):
        return self.dono
    
    def saiu_tela(self):
        if self.tamanho > self.tamanho_maximo:
            return True
        return False

    def get_dano(self):
        return self.dano
    
    def get_dono(self):
        return self.dono




