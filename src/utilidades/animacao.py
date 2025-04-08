import pygame

class Animation:
    def __init__(self, idle, attacking=None, jumping=None, others = None, numbers_frame = 5):
        self.idle = idle # parado
        self.attack = attacking # atackando
        self.jump = jumping #pulando
        self.others = others # Para NPC
        self.frame_atual = 0 # contador
        self.animation_atual = self.idle # animação atual
        self.frames_atualizacao = numbers_frame # atualiza frame
        self.contador_frames = 0 # numero passado

    def update(self):
        self.contador_frames+=1
        if self.contador_frames > self.frames_atualizacao:
            self.contador_frames = 0
            self.frame_atual = (self.frame_atual + 1 ) % len(self.animation_atual)

    def get_frame(self):
        return self.animation_atual[self.frame_atual]
    

    def change_state(self, state):
        if state == "attack" or state == "ataque":
            self.animation_atual = self.attack
        elif state == "idle" or state == "parado":
            self.animation_atual = self.idle
        elif state == "others" or state == "outros":
            self.animation_atual = self.others
    

    def draw(self, screen, position):
        nova_posicao = self.animation_atual[self.frame_atual].get_rect(center = position)
        screen.blit(self.animation_atual[self.frame_atual], nova_posicao)
    


class ImageHandler:
    def __init__(self):
        self.animations = {}
    
    def add_animation(self, name, animation):
        self.animations[name] = animation
    
    def update(self, name):
        if name in self.animations:
            self.animations[name].update() 
    
    def change_state(self, name, state):
        if name in self.animations:
            self.animations[name].change_state(state)
    
    def draw(self, surface, name, position):
        if name in self.animations:
            self.animations[name].draw(surface, position)





    
