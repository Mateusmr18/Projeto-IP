import pygame
from pygame import mouse, font, Vector2

class MenuBotao:
    def __init__(self, texto, posicao, cor, cor_hover, fonte, retorno = None):
        self.texto = texto
        self.posicao = posicao
        self.cor = cor
        self.cor_hover = cor_hover
        self.fonte = fonte
        self.retorno = retorno

    def desenhar(self, tela, selecionado = False):


        cor = None
        if selecionado:
            cor = self.cor_hover
        else:
            cor = self.cor


        texto = self.fonte.render(self.texto, True, cor)
        medidas_texto = Vector2(texto.get_size())
        posicao_retangulo = texto.get_rect(center=(self.posicao))
        tela.blit(texto, posicao_retangulo)

    
    def foi_pressionado(self):
        return self.retorno
    