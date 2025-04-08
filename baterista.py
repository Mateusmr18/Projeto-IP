import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
fundo = pygame.image.load("palco_slipquinoti.png").convert()
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))  # ajusta ao tamanho da tela
tela.blit(fundo, (0, 0))
pygame.display.set_caption("The Last Song")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
CINZA = (100, 100, 100)
MARROM = (139, 69, 19)

# Iniciar música
pygame.mixer.init()
musica = ""
pygame.mixer.music.load(musica)
pygame.mixer.music.play()

# Classe do Jogador
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.centery = ALTURA // 2
        self.rect.left = LARGURA - 10
        self.velocidade = 4
        self.tem_bateria = False

        #'piscagem' do jogador ao receber dano
        self.piscar = False
        self.tempo_piscar = 250
        self.timer_piscar = 0 #tempo da piscada

        self.vida_maxima = 20
        self.vida_atual = self.vida_maxima

    def receber_dano(self):
        self.vida_atual -= 1
        self.piscar = True
        self.timer_piscar = pygame.time.get_ticks()

    def update(self):
        teclas = pygame.key.get_pressed()
        tempo_atual = pygame.time.get_ticks()
        if teclas[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_d] and self.rect.right < LARGURA:
            self.rect.x += self.velocidade
        if teclas[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.velocidade
        if teclas[pygame.K_s] and self.rect.bottom < ALTURA:
            self.rect.y += self.velocidade
        if self.piscar:
            if tempo_atual - self.timer_piscar > self.tempo_piscar: #depois de 250ms, o personagem para de piscar
                self.piscar = False
                self.image.set_alpha(255)
            else: #alterna entre exibir e apagar o personagem
                if (tempo_atual // 2) % 2 == 0:
                    self.image.set_alpha(0)
                else:
                    self.image.set_alpha(255)
        else:
            self.image.set_alpha(255)
        if self.vida_atual <= 0:
            print("Você Morreu")
            self.kill()

    def barra_vida(self, superficie):
        largura = 100
        altura = 15
        espacos = 20
        largura_espaco = largura // espacos

        x = self.rect.centerx - largura // 2
        y = self.rect.top - 30

        pygame.draw.rect(superficie, BRANCO, (x - 2, y - 2, largura + 4, altura + 4), 2) #contorno da barra de vida

        for i in range(espacos): #desenha e apagas os quadradinhos verdes que representam a vida
            cor = VERDE if i < self.vida_atual else CINZA
            pygame.draw.rect(superficie, cor, (x + i * largura_espaco, y, largura_espaco - 2, altura))
    
    def pegar_bateria(self):
        self.tem_bateria = True

class BossBaterista(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill(VERMELHO)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA // 2
        self.rect.top = 380
        
        #lanca ataques aleatoriamente
        self.tempo_ataque = random.randint(500, 1000)
        self.ultimo_ataque = pygame.time.get_ticks()
        

        self.piscar = False
        self.tempo_piscar = 500
        self.timer_piscar = 0

        self.vida_maxima = 30
        self.vida_atual = self.vida_maxima

    def tomar_dano(self):
        self.vida_atual -= 1
        self.piscar = True
        self.timer_piscar = pygame.time.get_ticks()

    def update(self):
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.ultimo_ataque >= self.tempo_ataque:
            self.ataque()
            self.ultimo_ataque = tempo_atual
            self.tempo_ataque = random.randint(500, 1000)
        
        if self.piscar:
            if tempo_atual - self.timer_piscar > self.tempo_piscar:
                self.piscar = False
                self.image.set_alpha(255)
            else:
                if (tempo_atual // 2) % 2 == 0:
                    self.image.set_alpha(0)
                else:
                    self.image.set_alpha(255)
        else:
            self.image.set_alpha(255)
            
        if self.vida_atual <= 0:
            print("Boss derrotado")
            bateria = Bateria()
            sprites.add(bateria)
            baterias.add(bateria)
            self.kill()
    
    def ataque(self):
        projetil_baterista = AtaqueBaterista(self.rect.centerx, self.rect.centery, jogador.rect.centerx, jogador.rect.centery, velocidade_projetil_boss)
        ataques_baterista.add(projetil_baterista)
        sprites.add(projetil_baterista)
    
    def barra_vida(self, superficie):
        largura = 150
        altura = 20
        espacos = 30
        largura_espaco = largura // espacos

        x = self.rect.centerx - largura // 2
        y = self.rect.top - 30

        pygame.draw.rect(superficie, BRANCO, (x - 2, y - 2, largura + 4, altura + 4), 2)

        for i in range(espacos):
            cor = VERDE if i < self.vida_atual else CINZA
            pygame.draw.rect(superficie, cor, (x + i * largura_espaco, y, largura_espaco - 2, altura))

class AtaqueBaterista(pygame.sprite.Sprite):
    def __init__(self, origem_x, origem_y, alvo_x, alvo_y, velocidade_projetil_boss):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect(center=(origem_x, origem_y))
        
        #calculo do tamanho do vetor distancia entre o boss e o personagem
        dx = alvo_x - origem_x
        dy = alvo_y - origem_y
        comprimento = (dx ** 2 + dy ** 2) ** 0.5

        self.vx = int((dx / comprimento) * velocidade_projetil_boss)
        self.vy = int((dy / comprimento) * velocidade_projetil_boss)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy


class Bateria(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(MARROM)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA // 2
        self.rect.top = 480

# Minigame - Classe dos retângulos
class Retangulo:
    def __init__(self, x, y, largura, altura, cor):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor
        self.visivel = True

    def desenhar(self, tela):
        if self.visivel:
            pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))

    def atualizar_posicao(self, delta_time, velocidade):
        if self.visivel:
            self.x += velocidade * delta_time
            if self.x >= 415:
                self.x = 216
        return 0

    def esconder(self):
        self.visivel = False

    def mostrar(self):
        self.visivel = True

    def resetar_posicao(self):
        self.esconder()
        self.x = 216  # Posição inicial
        self.y = 560  # Posição inicial
        self.mostrar()  # Garante que o retângulo está visível novamente


#VARIAVEIS GLOBAIS:
velocidade_projetil_boss = 12
fonte = pygame.font.SysFont("arial", 48)

# Instâncias dos objetos
sprites = pygame.sprite.Group()
ataques_baterista = pygame.sprite.Group()
baterias = pygame.sprite.Group()

jogador = Jogador()
chefe = BossBaterista()
sprites.add(jogador, chefe)

# Minigame config
inicio_jogo = pygame.time.get_ticks()
tempo_espera = 24000
rect_speed = 430
retangulo_1 = Retangulo(398, 550, 4, 50, (VERMELHO))
retangulo_2 = Retangulo(219, 560, 30, 30, (VERDE))

# Estados do jogo
jogo_ativo = True
jogo_encerrado = False

# Loop do jogo
relogio = pygame.time.Clock()
rodando = True
while rodando:
    delta_time = relogio.tick(60) / 1000 #TEMPO ENTRE FRAMES
    tempo_decorrido = pygame.time.get_ticks() - inicio_jogo

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and jogo_ativo:
                if retangulo_2.visivel:
                    if 330 <= retangulo_2.x <= 440: #tolerancia para acerto do time da musica
                        chefe.tomar_dano()
                    else:
                        jogador.receber_dano() #se errar o time toma dano
                    retangulo_2.resetar_posicao()
            elif evento.key == pygame.K_r and jogo_encerrado:
                # Reinicia o jogo
                jogador = Jogador()
                chefe = BossBaterista()
                sprites.empty()
                sprites.add(jogador, chefe)
                ataques_baterista.empty()
                baterias.empty()
                inicio_jogo = pygame.time.get_ticks()
                retangulo_1 = Retangulo(398, 550, 4, 50, (VERMELHO))
                retangulo_2.resetar_posicao()
                pygame.mixer.music.play()
                jogo_ativo = True
                jogo_encerrado = False

    if jogo_ativo:
        sprites.update()

        colisoes = pygame.sprite.spritecollide(jogador, ataques_baterista, True)
        if colisoes:
            jogador.receber_dano() #se oprojetil do boss acertar o jogador, ele recebe dano

        colisoes_bateria = pygame.sprite.spritecollide(jogador, baterias, True)
        for bateria in colisoes_bateria:
            jogador.pegar_bateria()

        tela.blit(fundo, (0, 0))
        sprites.draw(tela)

        if tempo_decorrido >= tempo_espera:
            retangulo_1.desenhar(tela)
            retangulo_2.desenhar(tela)
            retangulo_2.atualizar_posicao(delta_time, rect_speed)

        if chefe.alive():
            chefe.barra_vida(tela)
        if jogador.alive():
            jogador.barra_vida(tela)
        else:
            jogo_ativo = False
            jogo_encerrado = True
            pygame.mixer.music.stop()

    else: #quando o personagem perde toda sua vida, aparece uma tela de game over
        tela.blit(fundo, (0, 0))
        texto = fonte.render("GAME OVER", True, VERMELHO)
        instrucoes = pygame.font.SysFont("arial", 24).render("Pressione R para reiniciar", True, BRANCO)
        tela.blit(texto, (LARGURA//2 - texto.get_width()//2, ALTURA//2 - 50))
        tela.blit(instrucoes, (LARGURA//2 - instrucoes.get_width()//2, ALTURA//2 + 10))

    pygame.display.flip()

pygame.quit()
