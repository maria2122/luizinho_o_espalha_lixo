import pygame
from scripts.animatedbg import AnimatedBg
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text
from scripts.player import Player
from scripts.fade import Fade
from scripts.camera import Camera
import random

class Game(Scene):
    def __init__(self):
        super().__init__()
        self.colision_sprites = pygame.sprite.Group()

        self.stage = 0
        self.maps = [MAP0, MAP1, MAP2]
        self.current_level = Level(self.maps[self.stage])
        self.active = True 

    def events(self, event):
        pass

    def draw(self):
        self.current_level.draw()

    def update(self):
        if self.current_level.active == False and self.current_level.gameover == False:

            self.stage += 1
            if len(self.maps) == self.stage:
                self.active = False
            else:
                self.current_level = Level(self.maps[self.stage])
        elif self.current_level.active == True and \
            self.current_level.gameover == True:

            self.active = False
        self.current_level.update()
   

class Ui:
    def __init__(self, gain):
        self.display = pygame.display.get_surface()
        self.ui_group = pygame.sprite.Group()
        
        self.gain = gain

    def count_gains(self, gain):
        if self.gain == 1:
            Obj("assets/player/lixeira64.png", [0,10], [self.ui_group])
           
        elif self.gain == 2:
            Obj("assets/player/lixeira64.png", [0,10], [self.ui_group])
            Obj("assets/player/lixeira64.png", [0,10], [self.ui_group])
        elif self.gain == 3:
            Obj("assets/player/lixeira64.png", [0,10], [self.ui_group])
            Obj("assets/player/lixeira64.png", [0,10], [self.ui_group])
            Obj("assets/player/lixeira64.png", [0,10], [self.ui_group])
        elif self.gain == 4:
            Obj("assets/player/lixeira64.png", [0,10], [self.ui_group])
            Obj("assets/player/lixeira64.png", [0,10], [self.ui_group])
            Obj("assets/player/lixeira64.png", [0,10], [self.ui_group])
            Obj("assets/player/lixeira64.png", [0,10], [self.ui_group])
        elif self.gain == 5:
            Obj("assets/player/lixeira64.png", [0,10], [self.ui_group])
            Obj("assets/player/lixeira64.png", [0,10], [self.ui_group])
            Obj("assets/player/lixeira64.png", [0,10], [self.ui_group])
            Obj("assets/player/lixeira64.png", [0,10], [self.ui_group])
            Obj("assets/player/lixeira64.png", [0,10], [self.ui_group])

    def draw(self):
        self.ui_group.draw(self.display)

    def update(self, gain):
        self.count_gains(gain)

class Level:
    def __init__(self, worldmap):

        self.display = pygame.display.get_surface()
        self.all_sprites = Camera()
        self.colision_sprites = pygame.sprite.Group()
        self.colision_trashes = pygame.sprite.Group()

        self.active = True
        self.fade = Fade(5)
        self.pts = 0
        self.score_text = Text("assets/fonts/airstrike.ttf",25, "Score: ", "brown", [30,30])
        self.score_pts = Text("assets/fonts/airstrike.ttf", 25, "0", "brown", [130, 30])
        self.hud_ui = Ui(self.pts)
        self.player = Player([100, 128], [self.all_sprites], self.colision_sprites, self.colision_trashes,
        self.pts, self.score_text, self.score_pts, self.hud_ui)

        self.worldmap = worldmap      
        self.generate_map()
        
        # A lixeira é criada na geração do mapa

    def events(self, event):
        pass

    # def next_stage(self):
    #     if self.player.rect.colliderect(self.finish.rect):
    #         self.active = False

    def reset_position(self):
        if self.player.rect.y > HEIGHT:
            self.player.rect.x = 0
            self.player.rect.y = 0

            self.hud_ui.gain -= 1

    def draw(self):
        self.all_sprites.costum_draw(self.player)
        self.hud_ui.draw()
        self.fade.draw()

    def generate_map(self):
        for row_index, row in enumerate(self.worldmap):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if col == 'X':
                    Obj("assets/title/tile.png", [x, y], [self.all_sprites, self.colision_sprites])

                elif col == 'C':
                    Trash("assets/player/lixeira64.png", [x, y], [self.all_sprites, self.colision_trashes])
                    
                elif col == 'P':
                    self.player.rect.x = x
                    self.player.rect.y = y

    def colision(self):
        pass

    def gameover(self):
        pass

    def update(self):
        self.all_sprites.update()
        self.player.update()
        self.score_text.draw()
        self.score_pts.draw()
        self.reset_position()
        

class Trash(Obj):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

    def update(self):
        return super().update()