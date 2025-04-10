from pygame import mixer
from assets import Assets

mixer.init() # inicia o mixer do pygame

class MusicManager():
    def __init__(self):
        self.biblioteca_musicas = {}
        self.musica_atual = None
        self.ta_tocando = False

    def add_music(self, nome_musica , arquivo_musica):
        self.biblioteca_musicas[nome_musica] = arquivo_musica
    

    def play_music(self, nome_musica, loop=-1, start = 0):
        if nome_musica in self.biblioteca_musicas:
            musica = self.biblioteca_musicas[nome_musica]

            if self.musica_atual != musica:
                self.musica_atual = musica

                mixer.music.load(musica)
                mixer.music.play(loops = loop, start=start)
                self.ta_tocando = True

    def pause_music(self):
        mixer.music.pause()

    
    def stop_music(self):
        mixer.music.stop()
        self.musica_atual = None
        self.ta_tocando = False

    def unpause_music(self):
        mixer.music.unpause()

    
    def set_volume(self, altura):
        mixer.music.stop()



toca_musica = MusicManager()
toca_musica.add_music("beto", Assets.rota('musicas/beethoven_nightmare.mp3'))
toca_musica.add_music("intro", Assets.rota("musicas/intro.mp3"))
toca_musica.add_music("kurt", Assets.rota("musicas/nirvana_teen.mp3"))
toca_musica.add_music("ganhou", Assets.rota("musicas/ganhou.mp3"))
