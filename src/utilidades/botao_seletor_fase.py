import pygame
from pygame import image, Vector2, Surface

class BotaoSeletorFase:
    def __init__(self, end_imagem , posicao, pega_musica, resposta_pressionado):
        self.imagem = image.load(end_imagem)
        self.posicao = posicao
        self.musica = pega_musica
        self.resposta_pressionada = resposta_pressionado

    def desenhar(self, tela, selecionado = False):

        lugar = self.posicao

        if selecionado == True:
            lugar = self.posicao + Vector2(0,-80)

        localizacao_imagem = self.imagem.get_rect(center = lugar)
        tela.blit(self.imagem, localizacao_imagem)

    def pega_musica(self):
        return self.musica

    def foi_pressionado(self):
        return self.resposta_pressionada