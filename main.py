import pygame
from src.fases.Fase1 import Fase1


TAMANHO = 800, 600
FPS = 60

class Jogo():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(TAMANHO)
        pygame.display.set_caption('Battle Music')
        self.relogio = pygame.time.Clock()
        self.screen.fill("purple")
        
        self.fase = Fase1(self.screen)
        
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