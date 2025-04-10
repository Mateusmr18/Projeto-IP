import pygame
from pygame import font
from pygame import Vector2
from assets import Assets

class ContadorVida(pygame.sprite.Sprite):
    def __init__(self, vidas, posicao):
        super().__init__()
        self.vidas = vidas
        self.image = pygame.Surface((48, 48))
        self.rect = self.image.get_rect()
        self.rect.center = posicao
        self.image_base = pygame.Surface((48, 48), pygame.SRCALPHA)
        self.fonte = pygame.font.Font(Assets.rota("fontes/MineMouseRegular.ttf"), 40)

    
    def mostra_vida(self):
        texto = self.fonte.render(f"{self.vidas}", True,(50, 20, 20))
        copia_base =  self.image_base.copy()
        
        centro_numero = (Vector2(copia_base.get_size()) - Vector2(texto.get_size())) // 2
        copia_base.blit(texto, centro_numero)
        self.image = copia_base
        
    def reduzir_vida(self, dano = 1):
        if self.vidas > 0:
            self.vidas-=dano

        self.mostra_vida()

    def ta_vivo(self):
        if self.vidas > 0:
            return True
        return False