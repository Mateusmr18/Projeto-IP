import pygame
import pytmx
from pygame import Surface
from pygame.math import Vector2

class Mapa():
    def __init__(self, mapa_jogo):
        self.carregar_mapa(mapa_jogo)

    def carregar_mapa(self, tmx):
        self.mapa_jogo = pytmx.load_pygame(tmx)
        self.tamanho_em_tiles = Vector2(self.mapa_jogo.width, self.mapa_jogo.height)
        self.tamanho_tiles = self.mapa_jogo.tilewidth
        self.surface = Surface(self.tamanho_em_tiles * self.tamanho_tiles)

    def pegar_tamanho_mapa(self):
        return self.tamanho_em_tiles * self.tamanho_tiles

    def pegar_tamanho_grid(self):
        return self.tamanho_em_tiles

    def desenhar_mapa(self):
        for layer in self.mapa_jogo.visible_layers:
            for x, y, gid, in layer:
                tile = self.mapa_jogo.get_tile_image_by_gid(gid)
                self.surface.blit(tile, (x * self.mapa_jogo.tilewidth, y * self.mapa_jogo.tileheight))

        return self.surface

    def pode_andar(self, nova_posicao):
        
        tamanho_x, tamanho_y = self.pegar_tamanho_mapa()

        if (nova_posicao.x >= 0 and nova_posicao.x < tamanho_x and 
            nova_posicao.y >= 0 and nova_posicao.y < tamanho_y):
            return True
        
        return False
            
    def pegar_centro_mapa(self):
        return (self.pegar_tamanho_mapa() // 48 )* 48 // 2
    