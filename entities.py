import json
import pygame

with open("settings.json", "r") as settingsFile:
    settings = json.load(settingsFile)


class player:
    def __init__(self):
        self.sprite = pygame.image.load("assets/spaceship.png")
        self.x = (settings["WIDTH"] * 0.45)
        self.y = (settings["HEIGHT"] * 0.8)
        self.x_change = 0
        self.y_change = 0
        self.health = 3 # Damage must = 1
    
    def updatePosition(self):
        self.x += self.x_change
        self.y += self.y_change

    def checkBorders(self):
        if self.y > 420:
            self.y = 420
        if self.y < -20:
            self.y = -20
        if self.x > 820:
            self.x = 820
        if self.x < -15:
            self.x = -15


class enemy:
    def __init__(self, xStart, yStart):
        self.sprite = pygame.transform.flip(pygame.image.load("assets/spaceship2.png"), False, True)
        self.x = xStart
        self.y = yStart
        self.x_change = 5
        self.y_change = 0
        self.health = 1
    
    def updatePosition(self):
        if self.x > 820:
            self.x_change = -5
        elif self.x < -15:
            self.x_change = 5
        self.x += self.x_change
        self.y += self.y_change