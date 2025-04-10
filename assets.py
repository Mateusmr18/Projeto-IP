import os

class Assets:
    ROTA_BASE = os.path.join(os.path.dirname(__file__), "assets")
    ROTA_DATA = os.path.join(os.path.dirname(__file__), "data")


    @staticmethod
    def rota(nome_arquivo):
        return os.path.join(Assets.ROTA_BASE, nome_arquivo)

    
    @staticmethod
    def data_rota(nome_arquivo):
        return os.path.join(Assets.ROTA_DATA, nome_arquivo)