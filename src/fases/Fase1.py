import pygame
from src.protagonista.protagonista import Protagonista
from src.mapa.mapa import Mapa
from src.fases.FaseBase import FaseBase


class Fase1(FaseBase):
    def __init__(self, tela):
        super().__init__("Battle Mozart")
        self.tela = tela
        self.grupo_sprites = pygame.sprite.Group()
        
        self.carregar_elementos()

    def carregar_elementos(self):
        self.mapa = Mapa("assets/mapa/Palco.jpeg")
        x, y = self.mapa.pegar_tamanho_mapa()
        
        self.protagonista = Protagonista(" ", (x // 2, y * 0.95), 10)
        self.protagonista.carregar_mapa(self.mapa)
        self.grupo_sprites.add(self.protagonista)

    def processar_eventos(self, eventos):
        
        teclas = pygame.key.get_pressed()
        self.protagonista.mover(teclas)

    def atualizar(self):
        pass

    def desenhar(self, tela):
        
        tela.fill("black")
        mapa = self.mapa.desenhar_mapa()
        self.grupo_sprites.draw(mapa)
        tela.blit(mapa, (0,0 ))


    def verifica_fim_fase(self):
        return False
    

