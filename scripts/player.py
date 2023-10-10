import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos,
                 groups,
                 colision_group):
        super().__init__(groups)
        self.image= pygame.image.load("assets/player/luiz_fumando-64.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.colision_group = colision_group
        self.speed=5
        self.jump_force = 18
        self.direction = pygame.math.Vector2()
        self.gravity =0.8

        # self.on_ground = False

        self.flip = False
        self.tick = 0
        self.frame = 0

    def move(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        # if self.on_ground == False:
        #     self.image = \
        #         pygame.image.load("assets/player/jump.png")
        #     self.image = pygame.transform.flip(
        #         self.image, self.flip, False)


    # def gravity_force(self):
    #     self.direction.y += self.gravity
    #     self.rect.y += self.direction.y

    def update(self):
        self.input()
        self.move()
        # self.gravity_force()
        # self.colision()
        self.y_colision()
        self.x_colision()

    def colision(self):
        for sprite in self.colision_group:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y>0: # baixo
                    self.direction.y = 0
                    self.rect.bottom = sprite.rect.top

                if self.direction.y < 0: # cima
                    self.direction.y = 0
                    self.rect.top = sprite.rect.bottom
                
                if self.direction.x < 0: #esquerda
                    self.direction.x = 0
                    self.rect.bottom = sprite.rect.top

                if self.direction.x > 0: # direita
                    self.direction.x = 0
                    self.rect.bottom = sprite.rect.top

    def y_colision(self):
        for sprite in self.colision_group:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y>0:
                    self.direction.y = 0
                    self.rect.bottom = sprite.rect.top

                if self.direction.y < 0:
                    self.direction.y = 0
                    self.rect.top = sprite.rect.bottom

    def x_colision(self):
        for sprite in self.colision_group:
            if sprite.rect.colliderect(self.rect):
                if self.direction.x>0:
                    self.direction.x = 0
                    self.rect.right = sprite.rect.left

                if self.direction.x < 0:
                    self.direction.x = 0
                    self.rect.left = sprite.rect.right

    def animation(self, speed, n_img, path):
        self.tick+=1
        if self.tick > speed:
            self.tick=0
            # self.frame= (self.frame+1) % n_img
            self.frame= (self.frame) % n_img
            self.image=pygame.image.load(
                # path+str(self.frame)+".png")
                path)
            self.image = pygame.transform.flip(
                self.image, self.flip, False)

    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.direction.x = -1
            self.flip = False # nao vira
            self.animation(8, 3, "assets/player/luiz_esquerda_correndo.png")
        elif key[pygame.K_d]:
            self.direction.x = 1
            self.flip = True 
            self.animation(8, 3, "assets/player/luiz_esquerda_correndo.png")#"assets/player/luiz_direita_correndo.png")
        elif key[pygame.K_s]:
            self.direction.y = 1
            self.flip = False 
            self.animation(8, 3, "assets/player/luiz_frente-64.png")
        elif key[pygame.K_w]:
            self.direction.y = -1
            self.flip = False 
            self.animation(8, 3, "assets/player/luiz_costas-64.png")
        else: #luiz_costas-64.png
            self.direction.x = 0
            self.direction.y = 0
            self.animation(16, 2, "assets/player/luiz_fumando-64.png")

        # if key[pygame.K_SPACE] and self.on_ground:
        #     self.direction.y=-self.jump_force
        #     self.on_ground = False