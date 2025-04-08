class GerenciadoFases:
    def __init__(self):
        self.fases = {}
        self.fase_atual = None

    def add_fases(self, nome, localizacao):
        self.fases[nome] = localizacao

    def change_fase(self, nome):
        if nome in self.fases:
            self.fase_atual = self.fases[nome]

    def desenhar(self, screen):
        self.fase_atual.desenhar(screen)

    
    def atualizar(self):
        self.fase_atual.atualizar()

    def processar_eventos(self, eventos):
        self.fase_atual.processar_eventos(eventos)