from pygame import Vector2, image
import time
from assets import Assets

class DiscoMovimento:
    def __init__(self, imagem , posicao, velocidade = 5):
        self.imagem = imagem
        self.posicao = Vector2(self.imagem.get_rect(center=posicao).topleft)
        self.velocidade = velocidade

    def change_velocidade(self, nova_velocidade):
        self.velocidade = Vector2(nova_velocidade)

    def update(self):
        self.posicao+= Vector2(0, self.velocidade)

    def draw(self, tela):
        tela.blit(self.imagem, self.posicao)


    def foi_acertado(self, trajeto_y, diferenca = 30):
        return abs(trajeto_y - self.posicao.y) < diferenca
    
    def get_position(self):
        return Vector2(self.posicao)
        


class DiscoFixo:
    def __init__(self, imagem , posicao, numero_frames_animacao = 5):
        self.imagem = imagem
        self.posicao = self.imagem.get_rect(center = posicao) #- (0, numero_frames_animacao * 2))
        self.animando = False
        self.numero_frames_animacao = numero_frames_animacao
        self.frame = 0

    def ativar(self):
        self.movendo = True
        self.frame = 0

    
    def update(self):
        if self.animando:
            self.frame+=1
            if self.frame > self.numero_frames_animacao:
                self.animando = False
    
    
    def draw(self, tela):
        if self.animando:
            tela.blit(self.imagem, self.posicao + (0, 1 * 2))
        else:
            tela.blit(self.imagem, self.posicao)



class Ritmo:
    def __init__(self, bpm):
        self.bpm = bpm
        self.intervalo_tempo = 60 / bpm # Frame para tempo
        self.ultima_batida = time.time()

    def update(self):
        agora = time.time()
        if agora - self.ultima_batida >= self.intervalo_tempo:
            self.ultima_batida = agora
            return True
        return False



class GameRitmo:
    def __init__(self, posicao, bpm):
        self.discos = []
        self.posicao = Vector2(posicao)
        self.alvo = DiscoFixo(image.load(Assets.rota('barra_ritmo/disco_vida.png')), posicao)
        self.imagem_disco_movimento = image.load(Assets.rota('barra_ritmo/disco_desce.png'))
        self.ritmo = Ritmo(bpm)

    def update(self):
        if self.ritmo.update():
            self.discos.append(self.enviar_discos())

        for disco in self.discos:
            if disco.get_position().y > 800:
                self.discos.remove(disco)
            else:
                disco.update()


    def enviar_discos(self):
        return DiscoMovimento(self.imagem_disco_movimento, (self.posicao.x, 50))


    def draw(self, tela):
        for disco in self.discos:
            disco.draw(tela)

        self.alvo.draw(tela)

    
    def tentar_acertar(self):
        self.alvo.ativar()
        for disco in self.discos:
            if disco.foi_acertado(self.posicao.y, 100):
                self.discos.remove(disco)
                return True

        return False