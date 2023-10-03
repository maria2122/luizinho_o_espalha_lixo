import pygame
from scripts.animatedbg import AnimatedBg
from scripts.scene import Scene
from scripts.text import Text
from scripts.obj import Obj
from scripts.settings import *
from scripts.button import Button
import sys

class GameOver(Scene):

    def __init__(self):
        super().__init__()
        self.bg = AnimatedBg("assets/menu/player/luiz_game_over.png",
                             [0, 0], [0, -HEIGHT], [self.all_sprites])
        self.title = Obj("assets/menu/title.png", [436, 166],
                         [self.all_sprites])

        self.btn_play = Button("white", 64, 520, "Return",
                               self.next_scene)
        self.btn_quit = Button("white", 64, 600, "Quit",
                               self.quit_game)

    def next_scene(self):
        self.active = False

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def events(self, event):
        self.btn_quit.events(event)
        self.btn_play.events(event)
        return super().events(event)

    def update(self):
        self.bg.update()
        self.btn_quit.draw()
        self.btn_play.draw()
        return super().update()




