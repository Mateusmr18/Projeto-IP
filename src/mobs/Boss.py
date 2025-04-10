
import pygame
from pygame import  draw
from pygame.math import Vector2

class BossBase(pygame.sprite.Sprite):
    def __init__(self, nome , img_manager, posicao_inicial, vida, mob_manager, player):
        pygame.sprite.Sprite.__init__(self)
        self.nome = nome
        self.animation = img_manager
        self.mob_manager = mob_manager
        self.player = player
        self.vida = vida
        self.entre_ataques = 60
        self.frames = 0 #Frames



        self.image = img_manager
        self.rect = self.image.get_rect()
        self.rect.center  = posicao_inicial

        self.angulo_protagonista = 0

    def pega_angulo(self):
        vetor_subtraido = self.player.get_posicao() - Vector2(self.rect.center)
        vetor_normalizado = Vector2(vetor_subtraido.normalize())
        self.angulo_protagonista = vetor_normalizado

    def get_hit(self, dano):
        self.vida -= dano

    def pega_posicao(self):
        return Vector2(self.rect.center)
    
    def get_nome(self):
        return self.nome
    
    def esta_morto(self):
        return self.vida <= 0

class BossBase2(pygame.sprite.Sprite):
    def __init__(self, nome , img_manager, posicao_inicial, vida, mob_manager, player):
        pygame.sprite.Sprite.__init__(self)
        self.nome = nome
        self.animation = img_manager
        self.animation.change_state(self.nome, "lutando")
        self.mob_manager = mob_manager
        self.player = player
        self.vida = vida
        self.entre_ataques = 60
        self.frames = 0

        self.image = self.animation.get_frame(self.nome)

        self.rect = self.image.get_rect()
        self.rect.center  = posicao_inicial

        self.angulo_protagonista = 0

    def update(self):
        self.animation.update(self.nome)
        self.image = self.animation.get_frame(self.nome)


    def pega_angulo(self):
        vetor_subtraido = self.player.get_posicao() - self.pega_posicao() 
        vetor_normalizado = vetor_subtraido.normalize()

        self.angulo_protagonista = vetor_normalizado

    def get_hit(self, dano):
        self.vida -= dano
        print(self.vida)

    def pega_posicao(self):
        return Vector2(self.rect.center)
    
    def get_nome(self):
        return self.nome
    
    def esta_morto(self):
        return self.vida <= 0
    

class Boss1(BossBase2):
    def __init__(self, nome , img_manager, posicao_inicial, vida, mob_manager, player):
        super().__init__(nome , img_manager, posicao_inicial, vida, mob_manager, player)

    def update(self):
        super().update()
        self.pega_angulo()
        self.attack()
        self.frames+=1

    def attack(self):
        if self.frames > 25:
            self.frames = 0
            self.mob_manager.shoot("normal", self.nome , self.rect.center, self.angulo_protagonista, 10, 1)
    

class Boss2(BossBase):
    def __init__(self, nome , img_manager, posicao_inicial, vida, mob_manager, player):
        super().__init__(nome , img_manager, posicao_inicial, vida, mob_manager, player)

    def update(self):
        super().update()
        self.pega_angulo()
        self.attack()
        self.frames+=1


    def attack(self):
        #if self.frames > 60*3:
        #    self.mob_manager.shoot("dancante", self.nome,  self.pega_posicao(), None, 1 , 1,  chegada = self.player.get_posicao() )
        #    self.frames = 0

        if self.frames > 120:
            self.frames = 0
            self.mob_manager.shoot("batidao", self.nome,  None, None, 1 , 1, )
        

        


class Boss3(BossBase2):
    def __init__(self, nome , img_manager, posicao_inicial, vida, mob_manager, player):
        super().__init__(nome , img_manager, posicao_inicial, vida, mob_manager, player)

    def update(self):
        super().update()
        self.pega_angulo()
        self.attack()

    def attack(self):
        self.frames+=1
       # self.mob_manager.shoot("normal", self.nome , self.rect.center, self.angulo_protagonista, 2, 1)
        #if self.frames > 30:
        #    self.frames=0
        #    self.mob_manager.shoot("dividido", self.nome,  self.pega_posicao(), None, 1 , 0,)

        
        #if self.frames > 25:
        #    self.mob_manager.shoot("dancante", self.nome,  self.pega_posicao(), None, 1 , 1,  chegada = self.player.get_posicao() )
        #    self.frames = 0

        if self.frames > 15:
            self.frames=0
            self.mob_manager.shoot("batidao", self.nome,  None, None, 1 , 1, )