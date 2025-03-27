from pygame.math import Vector2

class CameraJogo():
    def __init__(self, player):
        self.player = player
        self.x, self.y = player.local().xy

    def atualizar(self):
        self.x, self.y = self.player.local().xy

    def movimentacao(self, caracteristica):
        return caracteristica - Vector2(self.x, self.y)
    

        
