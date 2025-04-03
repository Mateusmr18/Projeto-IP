class FaseBase():
    def __init__(self, nome):
        self.nome = nome
        self.objetos = []
        self.cor_fundo = (0, 0, 0)


    def carregar_elementos(self):
        # Adiciona coisa que vai acontecer
        raise NotImplementedError("Tem que Implementar")
    
    def processar_eventos(self):
        # Comandos do player
        raise NotImplementedError("Tem que Implementar")
    
    def atualizar(self):
        # Atualiza para mostrar
        raise NotImplementedError("Tem que Implementar")
    
    def desenhar(self, tela):
        #O que vai ser mostrado na tela

        tela.fill(self. cor_fundo)  # Desenha o fundo
        # Aqui você pode desenhar os objetos da fase, inimigos, itens, etc.
        for objeto in self.objetos:
            objeto.desenhar(tela)

        raise NotImplementedError("Tem que Implementar")
    
    def verificar_fim_fase(self):

        raise NotImplementedError("Tem que Implementar")
    
