import pygame
from pygame import Vector2, image
from src.protagonista.protagonista import Protagonista
from src.mapa.mapa import Mapa
from src.fases.FaseBase import FaseBase
from src.utilidades.contador_vida import ContadorVida
from src.utilidades.timer_atack import GameRitmo
from src.mobs.mobmanager import MobManager
from src.mobs.Boss import Boss1, Boss2


class Fase1(FaseBase):
    def __init__(self, gerenciador):
        super().__init__("Battle Bethooven")
        self.gerenciador = gerenciador
        self.grupo_sprites = pygame.sprite.Group()
        self.mob_manager = MobManager()
        self.ritmo = GameRitmo(Vector2(800 * 0.95, 600 * 0.95), 120)
        self.carregar_elementos()

    def carregar_elementos(self):
        self.mapa = Mapa("assets/mapa/palcu_teatro_mozart.png") #Mapa

        x, y = self.mapa.pegar_tamanho_mapa()

        self.contador_vida = ContadorVida(3, (x * 0.95, y* 0.95))
        self.protagonista = Protagonista("prota", "", (x // 2, y), self.contador_vida, self.mob_manager)
        self.protagonista.carregar_mapa(self.mapa)

        boss = Boss2("Beethoven", image.load('assets/bosses/beethoven/beethoven_idle1.png'), Vector2(400, 300), 100, self.mob_manager, self.protagonista)


        self.mob_manager.add_mob(self.protagonista)
        self.mob_manager.add_mob(boss)

        
        self.contador_vida.mostra_vida()
        self.grupo_sprites.add(self.contador_vida)


    def processar_eventos(self, eventos):
        
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_z:
                    if self.ritmo.tentar_acertar():
                        self.protagonista.attack()
            
        teclas = pygame.key.get_pressed()
        self.protagonista.mover(teclas)

    def atualizar(self):
        self.mob_manager.update()
        self.ritmo.update()
        self.contador_vida.mostra_vida()

    def desenhar(self, tela):
        
        tela.fill("black")
        mapa = self.mapa.desenhar_mapa()
        self.mob_manager.draw(mapa)
        self.ritmo.draw(mapa)
        self.grupo_sprites.draw(mapa)

        tela.blit(mapa, (0,0 ))


    def verifica_fim_fase(self):
        return False
    

