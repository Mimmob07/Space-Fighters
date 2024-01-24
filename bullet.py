import math
import pygame


class bullet:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 90
        self.active = False
        self.sprite = pygame.image.load("assets/bullet.png")
        self.speed = 5
    
    def updatePosition(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        if self.y < 0:
            self.active = False


class bulletPool:
    def __init__(self):
        self.pool = []
        for i in range(30):
            bul = bullet()
            self.pool.append(bul)
    
    def grabBullet(self):
        for bul in self.pool:
            if not bul.active:
                return bul
        return False