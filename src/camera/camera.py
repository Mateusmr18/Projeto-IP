from pygame.math import Vector2

class Camera():
    def __init__(self, player):
        self.player = player
        self.posicao_camera = Vector2(0, 0)

    def atualizar(self):
        self.posicao_camera = Vector2(self.player.pegar_posicao())

    def posicao_desenhar(self):
        return  -self.posicao_camera
    

        
