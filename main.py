import json
import pygame
import discord
import threading
from bullet import Bulletpool
from discord import GSInstance
from entities import Player, Enemy

global player1
player1 = Player()
global enemy1
enemy1 = Enemy(401.5, 0)
global player_bullets
player_bullets = Bulletpool()
SP = discord.SpaceGameRPC()
RPCThread = threading.Thread(target=SP.start)
RPCThread.daemon = True
RPCThread.start()
with open("settings.json", "r") as settingsFile:
    settings = json.load(settingsFile)
# Remove flag to unscale if window appears too large
WIN = pygame.display.set_mode((settings["WIDTH"], settings["HEIGHT"]), flags=pygame.SCALED)
bg = pygame.image.load("assets/bg.png")
spaceship2 = pygame.image.load("assets/spaceship2.png")
pygame.init()
clock = pygame.time.Clock()
alive = True


def button(window, position, text):
    font = pygame.font.SysFont("impact", 50)
    text_render = font.render(text, True, (255, 255, 255))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(window, (150, 150, 150), (x, y), (x + w, y), 0)
    pygame.draw.line(window, (150, 150, 150), (x, y - 2), (x, y + h), 0)
    pygame.draw.line(window, (50, 50, 50), (x, y + h), (x + w, y + h), 0)
    pygame.draw.line(window, (50, 50, 50), (x + w, y + h), [x + w, y], 0)
    return window.blit(text_render, (x, y))


def draw_window():
    WIN.blit(bg, (0, 0))
    global b1
    b1 = button(WIN, (50, 120), "Start game")
    global b2
    b2 = button(WIN, (50, 190), "Settings")
    global b3
    b3 = button(WIN, (50, 260), "Quit")
    if GSInstance.GAMESTATE == GSInstance.states[1]:
        draw_game()
        pygame.display.update()
    else:
        pygame.display.update()


def draw_game():

    WIN.blit(bg, (0, 0))
    font = pygame.font.SysFont("Arial", 20)

    local_fps = str(clock.get_fps())
    local_fps = local_fps.split(".")
    text_render = font.render(local_fps[0], True, (255, 255, 255))
    WIN.blit(text_render, (0, 0))

    if player1.health >= 0:
        player1.update()
        player_rect = WIN.blit(player1.sprite, (player1.x, player1.y))
    else:
        GSInstance.set_gamestate(0)
    if enemy1.health >= 0:
        enemy1.update()
        enemy_rect = WIN.blit(enemy1.sprite, (enemy1.x, enemy1.y))
    else:
        enemy1.kill()

    for bullet in player_bullets.pool:
        if bullet.active:
            bul = WIN.blit(bullet.sprite, (bullet.x, bullet.y))
            if enemy1.health >= 0:
                if bul.colliderect(enemy_rect):
                    enemy1.health -= player1.damage
                    bullet.active = False

    for bullet in enemy1.bullets.pool:
        if bullet.active:
            bul = WIN.blit(bullet.sprite, (bullet.x, bullet.y))
            if player1.health >= 0:
                if bul.colliderect(player_rect):
                    player1.health -= enemy1.damage
                    bullet.active = False


def draw_settings():
    WIN.blit(bg, (0, 0))
    font = pygame.font.SysFont("impact", 20)
    # TODO


while alive:
    clock.tick(settings["FPS"])
    draw_window()
    pygame.display.set_caption("Space Fighters - " + GSInstance.GAMESTATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if b1.collidepoint(pygame.mouse.get_pos()):
                GSInstance.set_gamestate(1)
                draw_window()
            elif b2.collidepoint(pygame.mouse.get_pos()):
                print("Settings Button Clicked")
            elif b3.collidepoint(pygame.mouse.get_pos()):
                alive = False
        elif event.type == pygame.KEYDOWN and GSInstance.GAMESTATE == GSInstance.states[1]:
            if event.key == pygame.K_ESCAPE:
                GSInstance.set_gamestate(0)
                draw_window()
            if event.key == pygame.K_LEFT:
                player1.x_change = -5
            elif event.key == pygame.K_RIGHT:
                player1.x_change = 5
            elif event.key == pygame.K_UP:
                player1.y_change = -5
            elif event.key == pygame.K_DOWN:
                player1.y_change = 5
            elif event.key == pygame.K_SPACE:
                bullet = player_bullets.grabBullet()
                bullet.active = True
                bullet.x = player1.x
                bullet.y = player1.y + 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player1.x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player1.y_change = 0

    for i in range(len(player_bullets.pool)):
        if player_bullets.pool[i].active:
            player_bullets.pool[i].updatePosition()
pygame.quit()
