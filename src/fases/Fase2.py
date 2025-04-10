import pygame
from pygame import Vector2, image
from src.protagonista.protagonista import Protagonista, Protagonista2
from src.mapa.mapa import Mapa
from src.fases.FaseBase import FaseBase
from src.utilidades.contador_vida import ContadorVida
from src.utilidades.timer_atack import GameRitmo
from src.mobs.mobmanager import MobManager
from src.mobs.Boss import Boss1, Boss2, Boss3, BossBase, BossBase2
from src.utilidades.animacao_fim_fase import AnimacaoFimFase
from src.utilidades.som import toca_musica
from src.utilidades.animacao import Animation2, ImageHandler2
from src.utilidades.carregador_json import CarregadorJSON
from assets import Assets
from src.utilidades.animacao import Animation2
from src.protagonista.progresso import progresso


class Fase2(FaseBase):
    def __init__(self, gerenciador):
        super().__init__("Battle Bethooven")
        self.gerenciador = gerenciador
        self.grupo_sprites = pygame.sprite.Group()
        self.mob_manager = MobManager()
        self.ritmo = GameRitmo(Vector2(800 * 0.95, 600 * 0.95), 120)
        self.animacao_fim = AnimacaoFimFase(60*4, image.load(Assets.rota("finais/bateria_fim.png")))
        self.musica = toca_musica
        self.image_handler = ImageHandler2()
        self.json = CarregadorJSON()


    def carregar_elementos(self):
        self.mob_manager.clean()
        
        #Mapa
        self.mapa = Mapa(Assets.rota("mapa/slipknot_reduzido.png")) #Mapa

        # Animacoes protagonista
        imgs_protagonista_pegas = (self.json.carregar_frames("animacao.json", "protagonista", 0.1))
        animacao_protagonista = Animation2(imgs_protagonista_pegas, "parado", 10)
        self.image_handler.add_animation("protagonista", animacao_protagonista)

        #vida Protagonista
        self.contador_vida = ContadorVida(3, (800 * 0.95, 600 * 0.95))
        # Protagonista
        self.protagonista = Protagonista2("protagonista", self.image_handler, (400, 600), self.contador_vida, self.mob_manager)
        
        # mapa pro protagonista
        self.protagonista.carregar_mapa(self.mapa)


        frames_boss = self.json.carregar_frames("animacao.json", "baterista", 0.2)
        animacao_boss = Animation2(frames_boss, "lutando", 5)
        self.image_handler.add_animation("baterista", animacao_boss)


        # Começo Boss
        boss = Boss3("baterista", self.image_handler , Vector2(400, 400), 5, self.mob_manager, self.protagonista)


        #self.mob_manager.add_mob(self.protagonista)
        self.mob_manager.add_mob(boss)
        self.mob_manager.add_mob(self.protagonista)

        
        self.contador_vida.mostra_vida()
        self.grupo_sprites.add(self.contador_vida)

        self.musica.stop_music()
        self.musica.play_music("beto")

    def processar_eventos(self, eventos):
        
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_z:
                    if self.ritmo.tentar_acertar():
                        self.protagonista.attack()


        teclas = pygame.key.get_pressed()
        if any(teclas) or self.protagonista.esta_pulando:
            self.protagonista.mover(teclas)


    def atualizar(self):

        if self.animacao_fim.ativada:
            self.animacao_fim.atualizar()

            if self.animacao_fim.concluida():
                self.gerenciador.change_fase("seletor")

            return

        self.mob_manager.update()
        self.ritmo.update()
        self.contador_vida.mostra_vida()


        if self.verifica_fim_fase():
            self.comecar_fim_fase()


    def desenhar(self, tela):
        tela.fill("black") # Reset Tela
        # Se Acabou
        if self.animacao_fim.ativada:
            self.animacao_fim.desenhar(tela)
            return

        # Pega Mapa
        mapa = self.mapa.desenhar_mapa()

        self.mob_manager.draw(mapa) #Boss
        self.ritmo.draw(mapa) # Discos
        self.grupo_sprites.draw(mapa) #Coracao
        tela.blit(mapa,(0,0))

    def verifica_fim_fase(self):

        for mob in self.mob_manager.get_mobs():
            if isinstance(mob , BossBase2):
                if mob.esta_morto():
                    return True
                
        
        return False

    def comecar_fim_fase(self):
        progresso.add_conquista("bateria")
        self.animacao_fim.iniciar()
    


    

