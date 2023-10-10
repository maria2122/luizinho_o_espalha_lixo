from turtle import width
import pygame
import sys
from scripts.animatedbg import AnimatedBg
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text
from scripts.button import Button

class Menu(Scene):

    def __init__(self):
        super().__init__()
        self.bg = Obj("assets/menu/bg.png", [0,0], #[0, -HEIGHT], 
                             [self.all_sprites])
        self.title = Obj("assets/menu/title.png", [int(WIDTH * 0.19531), int(HEIGHT * 0.10416)],
                         [self.all_sprites])

        self.btn_play = Button("white", 64, 520, "Jogar",
                               self.next_scene)
        self.btn_quit = Button("white", 64, 600, "Sair",
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