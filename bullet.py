import pygame


class Bullet:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.active = False
        self.sprite = pygame.image.load("assets/bullet.png")
        self.speed = -5
    
    def updatePosition(self):
        self.y += self.speed
        if self.y < 0 or self.y > 500:
            self.active = False


class Bulletpool:
    def __init__(self):
        self.pool = []
        for i in range(30):
            bul = Bullet()
            self.pool.append(bul)
    
    def grabBullet(self):
        for bul in self.pool:
            if not bul.active:
                return bul
        return False
