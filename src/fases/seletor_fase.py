from src.fases.FaseBase import FaseBase

from src.fases.Fase1 import Fase1
from src.fases.Fase2 import Fase2
from src.objetos.caixa_som import ObjetoCenarioAnimado, ObjetoCenario

from src.utilidades.botao_seletor_fase import BotaoSeletorFase
from src.utilidades.animacao import Animation, ImageHandler
from src.utilidades.barra_conquistas import BarraConquistas

from pygame import Vector2, image
import pygame
from src.utilidades.som import toca_musica

class SeletorFase(FaseBase):
    def __init__(self, gerenciador):
        super().__init__("seletor")

        self.gerenciador = gerenciador
        self.hover = 0

        self.imagems = ImageHandler()
        self.cenario = []

        self.musica = toca_musica


        self.carregar_elementos()


    
    def carregar_elementos(self):

        animacao_som = Animation(None, None, None, [image.load(f"assets/objetos/caixa_som/sonzao{i}.png") for i in range(1, 4)], 20)
        self.imagems.add_animation("caixa_som", animacao_som)

       

        self.cenario.append(ObjetoCenario('mesa', image.load("assets/objetos/mesa/mesa.png")))
        self.cenario.append(ObjetoCenarioAnimado( self.imagems, "caixa_som",(850, 300)))
        
        tamanho_monitor = Vector2(800, 600)
        self.botoes = [
           
            BotaoSeletorFase("./assets/cds/cd_kurt.png",(tamanho_monitor.x * 0.3, tamanho_monitor.y * 0.7), "kurt" ,"fase3"),
            BotaoSeletorFase("./assets/cds/cd_slipknott.png",(tamanho_monitor.x * 0.3, tamanho_monitor.y * 0.8), "kurt","fase1"),
            BotaoSeletorFase("./assets/cds/cd_beto.png",(tamanho_monitor.x * 0.3, tamanho_monitor.y * 0.9), "beto", "fase1"),
            BarraConquistas("./assets/objetos/barra_conquista/barra_conquista.png",(tamanho_monitor.x * 0.5, tamanho_monitor.y * 1.05), "", "")
        ]


    def processar_eventos(self, eventos):
        for evento in eventos:
           #print(evento)
            if evento.type == pygame.QUIT:
                return False
            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    self.hover = (self.hover - 1) % len(self.botoes)
                
                if evento.key == pygame.K_DOWN:
                    self.hover = (self.hover + 1) % len(self.botoes)

                if evento.key == pygame.K_RETURN:
                    fase = self.botoes[self.hover].foi_pressionado()
                    if fase != "":
                        self.gerenciador.change_fase(fase)
                else:
                    self.musica.play_music(self.botoes[self.hover].pega_musica(), start = 100)
    
    def atualizar(self):
        for item in self.cenario:
            item.update()
    
    def desenhar(self, tela):

        for item in self.cenario:
            item.draw(tela)


        for n , botao in enumerate(self.botoes):
            botao.desenhar(tela, self.hover == n)
    
    def verificar_fim_fase(self):

        raise NotImplementedError("Tem que Implementar")
    
        