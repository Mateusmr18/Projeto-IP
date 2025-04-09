import pygame
from  src.mobs.Projetil import Projetil, NotaVibra, NotaDivide, LittleShots


class MobManager:
    def __init__(self):
        self.mobs = pygame.sprite.Group()
        self.projeteis = pygame.sprite.Group()
    
    def add_mob(self, personagem):
        self.mobs.add(personagem)
    

    def update(self):
        self.mobs.update()

        #Verifica Colisoes
        for projetil in self.projeteis:
            mobs_levaram = pygame.sprite.spritecollide(projetil, self.mobs, False) # Oh False é para tipo não dar hitkill
            for mob in mobs_levaram:
                if projetil.get_dono() != mob.get_nome():
                    mob.get_hit(projetil.get_dano())
                    projetil.kill()
        
        #Verifica Sair Tela
        for projetil in self.projeteis:
            if projetil.saiu_tela():
                projetil.kill()
            
        self.projeteis.update()


    def shoot(self, tipo, dono , posicao ,vetor_direcao = (0,0), velocidade = 10, dano = 1, **kargs):
        projetil = None
        if tipo == "normal":
            projetil = Projetil(dono, posicao, vetor_direcao, velocidade, dano)
        
        if tipo == "dancante":
            projetil = NotaVibra(dono, posicao, velocidade, dano, chegada = kargs["chegada"])

        if tipo == "dividido":
            projetil = NotaDivide(dono, posicao, self, velocidade, dano)

        if tipo == "pequenina":
            projetil = LittleShots(dono, posicao, vetor_direcao, velocidade, dano)

            
        if projetil != None:
            self.projeteis.add(projetil)
            print(self.projeteis)



    def draw(self, tela):
        self.projeteis.draw(tela)
        self.mobs.draw(tela)
