import json
from pygame import image, transform
from assets import Assets
class CarregadorJSON:
    def __init__(self):
        self.caminho_json = Assets.ROTA_DATA
    
    def carregar_frames(self, nome_arquivo, nome_item, porcentagem = 1.0):
        """Carrega o arquivo JSON e retorna os dados como um dicionário."""
        with open(Assets.data_rota(nome_arquivo), 'r') as f:
            dados = json.load(f)

        dados_item = dados[nome_item]
        animacoes = {}

        for titulo_animacao, dados in dados_item.items():
            prefixo = dados["prefixo"]
            animacoes[titulo_animacao] = self.transforma_imagem(prefixo, dados["quantidade_frames"], porcentagem)

        return animacoes
    

    def transforma_imagem(self, prefixo, quantidade_frames, porcentagem):
        frames = []
        for i in range(1, quantidade_frames + 1):
            imagem = image.load(Assets.rota(f"{prefixo}{i}.png"))
            if porcentagem != 1.0:
                imagem = transform.scale_by(imagem, porcentagem)
            frames.append(imagem)
        
        return frames
                       