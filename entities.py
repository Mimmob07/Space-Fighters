import json
import pygame
import time
from bullet import Bulletpool

with open("settings.json", "r") as settingsFile:
    settings = json.load(settingsFile)


class Player:
    def __init__(self):
        self.sprite = pygame.image.load("assets/spaceship.png")
        self.x = (settings["WIDTH"] * 0.45)
        self.y = (settings["HEIGHT"] * 0.8)
        self.x_change = 0
        self.y_change = 0
        self.damage = 1
        self.health = 3

    def update(self):
        self.x += self.x_change
        self.y += self.y_change

        if self.y > 420:
            self.y = 420
        if self.y < -20:
            self.y = -20
        if self.x > 820:
            self.x = 820
        if self.x < -15:
            self.x = -15


class Enemy:
    def __init__(self, xStart, yStart):
        self.sprite = pygame.transform.flip(pygame.image.load("assets/spaceship2.png"), False, True)
        self.x = xStart
        self.y = yStart
        self.x_change = 3
        self.y_change = 0
        self.bullets = Bulletpool()
        self.damage = 1
        self.health = 1
        self.lastshot = time.time()
    
    def update(self):
        if self.x > 820:
            self.x_change = -3
        elif self.x < -15:
            self.x_change = 3
        self.x += self.x_change
        self.y += self.y_change
        bullet = self.bullets.grabBullet()
        if (time.time() - self.lastshot) > 1:
            bullet.active = True
            bullet.x = self.x
            bullet.y = self.y
            bullet.speed = 5
            self.lastshot = time.time()
        for bul in self.bullets.pool:
            if bul.active:
                bul.updatePosition()

    def kill(self):
        for bul in self.bullets.pool:
            if bul.active: bul.active = False
