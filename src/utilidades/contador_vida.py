import pygame
from pygame import font
from pygame import Vector2

class ContadorVida(pygame.sprite.Sprite):
    def __init__(self, vidas, posicao):
        pygame.sprite.Sprite.__init__(self)
        self.vidas = vidas
        self.image = pygame.Surface((48, 48))
        self.rect = self.image.get_rect()
        self.rect.center = posicao
        self.image_base = pygame.Surface((48, 48), pygame.SRCALPHA)
        self.fonte = pygame.font.Font("./assets/fontes/MineMouseRegular.ttf", 40)

    
    def mostra_vida(self):
        texto = self.fonte.render(f"{self.vidas}", True,(50, 20, 20))
        copia_base =  self.image_base.copy()
        
        centro_numero = (Vector2(copia_base.get_size()) - Vector2(texto.get_size())) // 2
        copia_base.blit(texto, centro_numero)
        self.image = copia_base
        
    def tomar_dano(self):
        if self.vidas > 0:
            self.vidas-=1

    def ta_vivo(self):
        if self.vidas > 0:
            return True
        return False