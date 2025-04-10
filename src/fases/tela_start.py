
import pygame
from pygame import image, Surface, Vector2, transform, mixer, font
from src.fases.FaseBase import FaseBase
from src.utilidades.menu_botao import MenuBotao

from src.fases.seletor_fase import SeletorFase

from assets import Assets

pygame.font.init()
pygame.mixer.init()

class Entrada(FaseBase):
    def __init__(self, gerenciador):
        super().__init__("Entrada")
        self.gerenciador = gerenciador
        self.vinil = image.load(Assets.rota("start/vinil_m.png"))
        self.logo = image.load(Assets.rota("start/logo2.png"))
        self.angulo_rotacao_vinil = 0
        self.contador_pulsar = 0
        self.mixer = mixer.music
        self.fonte = font.Font(Assets.rota("fontes/MineMouseRegular.ttf"), 40)
        self.hover = 0

        self.estado_jogo = "escolhendo fase"


        self.carregar_elementos()

    
    def carregar_elementos(self):
        self.mixer.load(Assets.rota("musicas/intro.mp3"))
        self.mixer.play(10, 0.0, 0)

        self.botoes = [
            MenuBotao(f"Começar", Vector2(400, 600 * 0.75), "white", "yellow", self.fonte, "seletor"),
            MenuBotao(f"Sair", Vector2(400, 600 * 0.85), "white", "yellow", self.fonte, "")
        ]

    def processar_eventos(self, eventos):

        for evento in eventos:
           # print(evento)
            if evento.type == pygame.QUIT:
                return False
            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    self.hover -=1
                    self.hover%=2
                
                if evento.key == pygame.K_DOWN:
                    self.hover +=1
                    self.hover%=2

                
                if evento.key == pygame.K_RETURN:
                    clicado = self.botoes[self.hover].foi_pressionado()              
                    self.gerenciador.change_fase(clicado)
                

            

    def atualizar(self):

        if self.estado_jogo == "fases":
            return self.botoes[self.hover].foi_pressionado()


        
        self.angulo_rotacao_vinil= (self.angulo_rotacao_vinil + 1)% 360
        self.disco_rotacionado = transform.rotate(self.vinil, self.angulo_rotacao_vinil)

        self.contador_pulsar = (self.contador_pulsar + 1) % 25

        if self.contador_pulsar > 13 and self.contador_pulsar < 25:
            tamanho_logo = 1 + 0.01 * (7 - abs(self.contador_pulsar - 19))
            self.movimento_logo =  transform.scale_by(self.logo, tamanho_logo)
        else:
            self.movimento_logo = self.logo


        if self.botoes[self.hover].foi_pressionado():
            return "iniciar"




    def desenhar(self, tela: Surface):
        
        tela.fill((16, 0, 21))
        
        centro_vinil = (Vector2(tela.get_size()) - Vector2(self.disco_rotacionado.get_size())) // 2
        tela.blit(self.disco_rotacionado, centro_vinil)

        centro_logo = (Vector2(tela.get_size()) - Vector2(self.movimento_logo.get_size())) // 2
        tela.blit(self.movimento_logo, centro_logo)
        
        
        for n, botao in enumerate(self.botoes):
            botao.desenhar(tela, n == self.hover)


