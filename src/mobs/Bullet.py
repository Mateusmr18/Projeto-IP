import pygame
from pygame import Surface

class Bullet(pygame.sprite.Sprite):
    def __init__(self, dono, imagem, posicao, vetor_direcao, velocidade = 10):
        super().__init__()
        self.dono = dono
        self.image = Surface((5, 5), posicao)
        self.image.fill("green")
        self.rect = self.image.get_rect(center = posicao)
        self.velocidade = velocidade * vetor_direcao

    
    def update(self):
        self.posicao+=self.velocidade

        if (self.posicao.x < 0 or self.posicao.x > 800 and
            self.posicao.y < 0 or self.posicao.y > 600):

            self.kill