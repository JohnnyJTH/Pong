import pygame
from random import randint

BLACK = (0,0,0)


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.surface = pygame.Surface([x, y])
        self.surface = self.surface.convert()
        self.surface.fill(BLACK)
        self.image = pygame.image.load("whiteball.png")
        self.ball_rect = pygame.Rect((0,0), (x, y))
        self.image = pygame.transform.scale(self.image, self.ball_rect.size)
        self.image = self.image.convert()
        self.surface.blit(self.image, self.ball_rect)
        
        self.velocity = [randint(4, 8), randint(-8, 8)]
        
        self.rect = self.surface.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)