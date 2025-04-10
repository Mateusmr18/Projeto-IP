class Progresso:
    def __init__(self):
        #guitarra, piano, bateria
        self.conquistas = []

    def add_conquista(self, nome_consquista):
        self.conquistas.append(nome_consquista)

    def get_conquistas(self):
        return self.conquistas



progresso = Progresso()