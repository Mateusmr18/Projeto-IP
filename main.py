import pygame
from src.fases.tela_start import Entrada
from src.fases.seletor_fase import SeletorFase
from src.fases.Fase1 import Fase1
from src.fases.Fase2 import Fase2
from src.fases.Fase3 import Fase3
from src.fases.gerenciador_fases import GerenciadoFases

gerenciador_fases = GerenciadoFases()
gerenciador_fases.add_fases("intro", Entrada(gerenciador_fases))
gerenciador_fases.add_fases("seletor", SeletorFase(gerenciador_fases))
gerenciador_fases.add_fases("fase1", Fase1(gerenciador_fases))
gerenciador_fases.add_fases("fase2", Fase2(gerenciador_fases))
gerenciador_fases.add_fases("fase3", Fase3(gerenciador_fases))

gerenciador_fases.change_fase("intro")


TAMANHO = 800, 600
FPS = 60

class Jogo:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(TAMANHO)
        pygame.display.set_caption('Battle Music')
        self.relogio = pygame.time.Clock()
        self.screen.fill("purple")
        
        self.fase = gerenciador_fases
        
    def processar_eventos(self):
        eventos = pygame.event.get()
    
        for evento in eventos:
            if evento.type == pygame.QUIT:
                return False

        self.fase.processar_eventos(eventos)

        return True
        
    def atualizar(self):
        self.fase.atualizar()

    def desenhar(self):
        self.screen.fill("black")
        self.fase.desenhar(self.screen)
        pygame.display.flip()       

    def executar(self):
        continuar = True
        while continuar:
            continuar = self.processar_eventos()
            self.atualizar()
            self.desenhar()
            self.relogio.tick(FPS)


        pygame.quit()

jogo = Jogo()
jogo.executar()