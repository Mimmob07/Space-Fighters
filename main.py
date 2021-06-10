import pygame


class GameState:
    def __init__(self):
        self.states = ["Main Menu", "Playing Game", "In Game Menu"]
        self.GAMESTATE = self.states[0]

    def set_gamestate(self, state):
        self.GAMESTATE = self.states[state]

    def get_gamestate(self):
        return self.GAMESTATE

    def get_states(self):
        return self.states


GSInstance = GameState()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("assets/bg.png")
FPS = 60
pygame.init()


def button(window, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(window, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(window, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(window, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(window, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(window, (100, 100, 100), (x, y, w, h))
    return window.blit(text_render, (x, y))


def draw_window():
    WIN.blit(bg, (0, 0))
    global b1
    b1 = button(WIN, (50, 120), "Start game")
    global b2
    b2 = button(WIN, (50, 190), "Quit")
    if GSInstance.get_gamestate() == GSInstance.get_states()[1]:
        WIN.blit(bg, (0, 0))
        pygame.display.update()
    else:
        pygame.display.update()


def main():
    clock = pygame.time.Clock()
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
                    run = False

    pygame.quit()


if __name__ == "__main__":
    main()
