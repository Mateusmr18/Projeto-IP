from src.utilidades.som import toca_musica


class AnimacaoFimFase:
    def __init__(self, duracao, imagem):
        self.duracao = duracao
        self.tempo_passado = 0
        self.ativada = False
        self.imagem = imagem
        self.musica = toca_musica
    
    def iniciar(self):
        self.musica.stop_music()
        self.musica.play_music("ganhou", 0)
        self.ativada = True
        self.tempo_passado = 0

    
    def atualizar(self):
        if self.ativada:
            if self.tempo_passado < self.duracao:
                self.tempo_passado+=1
            else:
                self.ativada = False

    
    def desenhar(self, tela):
        tela.blit(self.imagem, (0,0))


        
    def concluida(self):
        return not self.ativada