import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BOOM
from pygame.sprite import Sprite

class Enemy(Sprite):
    SPEED_Y = 1
    SPEED_X = 1
    X_POS_LIST = [100, 150, 200, 250, 300, 350, 400, 450]
    Y_POS = 20
    LEFT = 'left'
    RIGHT = 'right'
    MOV_X = [LEFT, RIGHT]
    INTERVAL = 100

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOV_X)
        self.index = 0
        self.is_alive = True
        # self.sound = BOOM

    def update(self):
        if(self.rect.y >= SCREEN_HEIGHT):
            self.is_alive = False
        self.move()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y += self.SPEED_Y
        if (self.mov_x ==  self.LEFT):
            self.rect.x -= self.SPEED_X
            if self.index > self.INTERVAL or self.rect.x <= 0:
                self.mov_x = self.RIGHT
                self.index = 0

        else:
            self.rect.x += self.SPEED_X
            if self.index > self.INTERVAL or self.rect.x >= SCREEN_WIDTH - self.rect.width:
                self.mov_x = self.LEFT
                self.index = 0

        self.index += 1
