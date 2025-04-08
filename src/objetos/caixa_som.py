class ObjetoCenarioAnimado:
    def __init__(self, handle_animacao, nome, posicao = (0,0)):
        self.nome = nome
        self.animacoes = handle_animacao
        self.posicao = posicao
        self.animacoes.change_state(nome, "others")
    
    def update(self):
        self.animacoes.update(self.nome)
    
    def draw(self, tela):
        self.animacoes.draw(tela, self.nome , self.posicao)

class ObjetoCenario:
    def __init__(self, nome, imagem, posicao = (0,0)):
        self.nome = nome
        self.imagem = imagem
        self.posicao = posicao

    def update(self):
        pass

    def draw(self, tela):
        tela.blit(self.imagem, self.posicao)    