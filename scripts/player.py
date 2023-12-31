import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, colision_group, colision_trashes, pts, score_text, score_pts, gain):
        super().__init__(groups)
        self.image = pygame.image.load("assets/player/luiz_fumando-64.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.colision_group = colision_group
        self.speed = 4
        self.direction = pygame.math.Vector2()
        self.trashes = colision_trashes
        self.tick = 0
        self.frame = 0

        self.level = 1
        self.pts = pts
        self.gain = gain
        self.score_pts = score_pts
        self.score_text = score_text

    def move_x(self):
        self.rect.x += self.direction.x * self.speed
        

    def move_y(self):
        self.rect.y += self.direction.y * self.speed
        self.colision()

    def update(self):
        self.input()
        self.move_x()
        self.move_y()

    def colision(self):

        for sprite in self.colision_group:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y < 0: #cima
                    self.rect.top = sprite.rect.bottom

                if self.direction.y > 0: #baixo
                    self.rect.bottom = sprite.rect.top
                
                if self.direction.x > 0: # direita
                    self.rect.right = sprite.rect.left

                if self.direction.x < 0: # esquerda
                    self.rect.left = sprite.rect.right
        
        for trash in self.trashes:
          if trash.rect.colliderect(self.rect):
                trash.kill()
                self.pts +=1
                self.score_pts.update_text_1(str(self.pts)) 
                self.gain.update(self.pts)
                self.gain.draw()      

    def animation(self, speed, n_img, path):
        self.tick+=1
        if self.tick > speed:
            self.tick=0
            self.frame= (self.frame) % n_img
            self.image=pygame.image.load(path)

    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.direction.x = -1
            self.move_x()
            self.animation(8, 3, "assets/player/luiz_esquerda_correndo.png")
        elif key[pygame.K_d]:
            self.direction.x = 1
            self.move_x()
            self.animation(8, 3, "assets/player/luiz_direita_correndo.png")
        elif key[pygame.K_s]:
            self.direction.y = 1
            self.move_y()
            self.animation(8, 3, "assets/player/luiz_frente-64.png")
        elif key[pygame.K_w]:
            self.direction.y = -1
            self.move_y()
            self.animation(8, 3, "assets/player/luiz_costas-64.png")
        else: #luiz_costas-64.png
            self.direction.x = 0
            self.direction.y = 0
            self.animation(16, 2, "assets/player/luiz_fumando-64.png")
