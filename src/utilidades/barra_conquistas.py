from pygame import Vector2, image
from src.utilidades.botao_seletor_fase import BotaoSeletorFase
from src.protagonista.progresso import progresso

from assets import Assets

class BarraConquistas(BotaoSeletorFase):
    def __init__(self, end_imagem , posicao, pega_musica, resposta_pressionado):

        super().__init__(end_imagem, posicao, "", "")
        self.conquistas = progresso
        self.icones = {
            "guitarra": image.load(Assets.rota("objetos/barra_conquista/icone_guitarra.png")),
            "bateria": image.load(Assets.rota("objetos/barra_conquista/icone_baqueta.png")),
            "piano": image.load(Assets.rota("objetos/barra_conquista/icone_piano.png"))
        }

    def desenhar(self, tela, selecionado = False):
        conquistas = self.conquistas.get_conquistas()

        lugar = self.posicao
        if selecionado == True:
            lugar = self.posicao + Vector2(0,-80)


        localizacao_imagem = self.imagem.get_rect(center = lugar)

        imagem_copiada = self.imagem.copy()
        if "guitarra" in conquistas:
            imagem_copiada.blit(self.icones['guitarra'], (208, 50))
        if "bateria" in conquistas:
            imagem_copiada.blit(self.icones['bateria'],(325, 50))
        if "piano" in conquistas:
            imagem_copiada.blit(self.icones["piano"], (413, 25))


        tela.blit(imagem_copiada, localizacao_imagem)