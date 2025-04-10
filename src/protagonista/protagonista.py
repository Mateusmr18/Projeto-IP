import pygame
from pygame import  draw, transform
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
    





class Protagonista2(pygame.sprite.Sprite):
    def __init__(self, nome , animation_handler, posicao_inicial, obj_vida, mob_manager):
        pygame.sprite.Sprite.__init__(self)
        self.nome = nome
        self.animation_handler = animation_handler
        self.animation_handler.change_state(self.nome, "parado")

        self.image = self.animation_handler.get_frame(self.nome)
        #self.image = self.imagem_base

        self.rect = self.image.get_rect()
        self.rect.bottomleft  = posicao_inicial
        
        self.velocidade = 10

        self.esta_pulando = False
        self.contador_pulo = 10
        self.lado = "direita"

        self.vida = obj_vida

        self.mob_manager = mob_manager


        self.clique = 0
    
    def mudar_sprite(self, atirar= False):

        opcoes = None
        animacoes = None


        if atirar: 
            animacoes = "bater"
        elif self.esta_pulando: 
            animacoes = "pular"
        elif self.lado != "cima": 
            animacoes = "andar"
        elif self.lado == "cima":
            animacoes = "costas"
        else:
            animacoes = "parado"


        self.animation_handler.change_state(self.nome, animacoes)

        frame = self.animation_handler.get_frame(self.nome)
        self.image = pygame.transform.flip(frame, "esquerda" == self.lado , False)
        
    def carregar_mapa(self, mapa):
        self.mapa = mapa

    def mover(self, entrada):
        #self.clique+=1
        #print(self.clique)
        movimento = Vector2(0,0)

        if entrada[pygame.K_LEFT]:
            movimento += (-self.velocidade, 0)
            self.lado = "esquerda"

        elif entrada[pygame.K_RIGHT]: 
            movimento += (+self.velocidade, 0)
            self.lado = "direita"
        
        elif entrada[pygame.K_UP]:
            movimento += (0, 0)
            self.lado = "cima"
        
        if entrada[pygame.K_SPACE] or self.esta_pulando:
            movimento += Vector2(self.pular())


        movimento_x = nova_posicao= Vector2(self.rect.bottomleft) + (0, movimento[1])
        movimento_y = nova_posicao= Vector2(self.rect.bottomleft) + (movimento[0], 0)


        pode_mudar_sprite = False

        if self.mapa.pode_andar(movimento_x):
            self.rect.bottomleft += Vector2(0, movimento[1])
            pode_mudar_sprite = True

        if self.mapa.pode_andar(movimento_y):
            self.rect.bottomleft += Vector2(movimento[0], 0)
            pode_mudar_sprite = True

        self.mudar_sprite()

        self.animation_handler.update(self.nome)

    def pular(self):
        self.esta_pulando = True

        y = 0

        if self.contador_pulo >= -10:
            y = (self.contador_pulo * abs(self.contador_pulo)) * 0.5
            self.contador_pulo -= 0.5
        else:
            self.contador_pulo = 10
            self.esta_pulando = False


        return (0, -y)

    def attack(self):
        movimento_tiro = {"esquerda": (-1, 0), "direita": (1, 0), "cima": (0 , -1)}.get(self.lado)
        
        self.mob_manager.shoot("normal", self.nome , self.rect.center, movimento_tiro, 10, 1)
    
    def get_hit(self, dano):
        self.vida.reduzir_vida(dano)

    def get_posicao(self):
        return Vector2(self.rect.center)
    
    def get_nome(self):
        return self.nome