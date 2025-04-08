import pygame
from pygame import Vector2
from src.protagonista.protagonista import Protagonista
from src.mapa.mapa import Mapa
from src.fases.FaseBase import FaseBase
from src.utilidades.contador_vida import ContadorVida
from src.utilidades.timer_atack import GameRitmo


class Fase1(FaseBase):
    def __init__(self, gerenciador):
        super().__init__("Battle Mozart")
        self.gerenciador = gerenciador
        self.grupo_sprites = pygame.sprite.Group()
        self.estado_jogo = "rodando"
        self.ritmo = GameRitmo(Vector2(800 * 0.95, 600 * 0.95), 120)
        self.carregar_elementos()

    def carregar_elementos(self):
        self.mapa = Mapa("assets/mapa/palcu_teatro_mozart.png") #Mapa

        x, y = self.mapa.pegar_tamanho_mapa()
        
        self.contador_vida = ContadorVida(3, (x * 0.95, y* 0.95))
        self.protagonista = Protagonista(" ", (x // 2, y * 0.95), 10, self.contador_vida)

        self.protagonista.carregar_mapa(self.mapa)
        self.grupo_sprites.add(self.protagonista)
        self.contador_vida.mostra_vida()
        self.grupo_sprites.add(self.contador_vida)

    def processar_eventos(self, eventos):
        
        teclas = pygame.key.get_pressed()
        self.protagonista.mover(teclas)

    def atualizar(self):
        self.ritmo.update()
        self.contador_vida.mostra_vida()

    def desenhar(self, tela):
        
        tela.fill("black")
        mapa = self.mapa.desenhar_mapa()

        self.ritmo.draw(mapa)
        self.grupo_sprites.draw(mapa)

        tela.blit(mapa, (0,0 ))


    def verifica_fim_fase(self):
        return False
    

