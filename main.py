import pygame
import discord
import threading
from discord import GSInstance

SP = discord.SpaceGameRPC()
RPCThread = threading.Thread(target=SP.start)
RPCThread.daemon = True
RPCThread.start()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("assets/bg.png")
FPS = 60
pygame.init()
clock = pygame.time.Clock()


def button(window, position, text):
    font = pygame.font.SysFont("impact", 50)
    text_render = font.render(text, True, (255, 255, 255))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(window, (150, 150, 150), (x, y), (x + w, y), 0)
    pygame.draw.line(window, (150, 150, 150), (x, y - 2), (x, y + h), 0)
    pygame.draw.line(window, (50, 50, 50), (x, y + h), (x + w, y + h), 0)
    pygame.draw.line(window, (50, 50, 50), (x + w, y + h), [x + w, y], 0)
    # pygame.draw.rect(window, (100, 100, 100), (x, y, w, h))
    return window.blit(text_render, (x, y))


def draw_window():
    WIN.blit(bg, (0, 0))
    global b1
    b1 = button(WIN, (50, 120), "Start game")
    global b2
    b2 = button(WIN, (50, 190), "Settings")
    global b3
    b3 = button(WIN, (50, 260), "Quit")
    if GSInstance.get_gamestate() == GSInstance.get_states()[1]:
        draw_game()
        pygame.display.update()
    else:
        pygame.display.update()


def draw_game():
    WIN.blit(bg, (0, 0))
    font = pygame.font.SysFont("Arial", 20)
    localfps = str(clock.get_fps())
    localfps = localfps.split(".")
    text_render = font.render(localfps[0], True, (255, 255, 255))
    WIN.blit(text_render, (0, 0))


def main():
    run = True
    while run:
        clock.tick(FPS)
        draw_window()
        pygame.display.set_caption("Space Fighters - " + GSInstance.get_gamestate())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    GSInstance.set_gamestate(1)
                    draw_window()
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    print("Settings Button Clicked")
                elif b3.collidepoint(pygame.mouse.get_pos()):
                    run = False

    pygame.quit()


if __name__ == "__main__":
    main()
