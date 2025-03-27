import pygame
from pygame import image, Surface, Vector2
from protagonista import Protagonista
from camera import CameraJogo


# Resoluções
TAMANHO_TILE = 48
ALTURA = 800
LARGURA = 600
ZOOM = 2

# Inicia o bruto
pygame.init()
tela = pygame.display.set_mode((ALTURA, LARGURA),pygame.RESIZABLE)
relogio = pygame.time.Clock()



#Fase
altura_fase = ALTURA // ZOOM
largura_fase = LARGURA // ZOOM
fase = Surface((altura_fase, largura_fase), )
fase.fill((0, 128, 255))


#dados_jogador
player = Protagonista("red" , altura_fase // 2, largura_fase // 2 , TAMANHO_TILE)

camera = CameraJogo(player)

rodando = True
while rodando:
    # Para sair do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.KEYDOWN:
            player.mover(event.key)


    tela.fill("dark blue")
    fase.fill("gray")

    camera.atualizar()
    player.desenhar(fase)
    tela.blit(pygame.transform.scale(fase, (altura_fase * ZOOM, largura_fase * ZOOM) ), camera.movimentacao(Vector2(altura_fase//2, largura_fase//2)) * ZOOM)
    
    pygame.display.flip()
    relogio.tick(60)  # Roda o relogio

pygame.quit()
