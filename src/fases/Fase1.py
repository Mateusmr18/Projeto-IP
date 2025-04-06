import pygame
from src.protagonista.protagonista import Protagonista
from src.mapa.mapa import Mapa
from src.fases.FaseBase import FaseBase
from src.camera.camera import Camera
from src.mobs.boss import BossKurt


class Fase1(FaseBase):
    def __init__(self):
        super().__init__("Battle Mozart")
        self.tamanho_tile = 48
        self.carregar_elementos()
    

    def carregar_elementos(self):
        self.mapa = Mapa("assets/teste2.tmx")
        centro_mapa = self.mapa.pegar_centro_mapa()

        self.player = Protagonista("red" , centro_mapa)
        self.player.carregar_mapa(self.mapa)

        #self.boss = BossKurt(centro_mapa,self. tamanho_tile, 1)
        self.camera = Camera(self.player)

        self.sprites = pygame.sprite.Group()
        #self.sprites.add(self.boss)
        self.sprites.add(self.player)

    def processar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                self.player.mover(evento.key)

    def atualizar(self):
        self.camera.atualizar()

    def desenhar(self, tela):

        surface_mapa = self.mapa.desenhar_mapa()
        self.sprites.draw(surface_mapa)

        tela.blit(surface_mapa, self.camera.posicao_desenhar())

    def verifica_fim_fase(self):
        return False
    

