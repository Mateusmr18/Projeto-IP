import pygame
from pygame import Surface, image
from pygame.math import Vector2

class Mapa():
    def __init__(self, mapa_jogo):
        self.carregar_mapa(mapa_jogo)

    def carregar_mapa(self, endereco_img):
        self.mapa_jogo = image.load(endereco_img)
        self.tamanho_mapa = self.mapa_jogo.get_size()

    def pegar_tamanho_mapa(self):
        return self.tamanho_mapa
    

    def desenhar_mapa(self):
        return self.mapa_jogo.copy()

    def pode_andar(self, nova_posicao):
        
        tamanho_x, _ = self.pegar_tamanho_mapa()

        if (nova_posicao.x >= 0 and nova_posicao.x < tamanho_x ):
            return True
        return False
            
    def centro_chao(self):
        tamanho_x, _ = self.pegar_tamanho_mapa()
        return tamanho_x // 2
    