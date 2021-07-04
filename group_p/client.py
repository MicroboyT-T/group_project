import pygame
from network import Network
import pickle
pygame.font.init()

width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

#Button interface part#
class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


#Window part#
def redrawWindow(win, game, p):
    win.fill((0,0,0))

    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 65)
        text = font.render("Menunggu Pemain Lain...", 1, (255,0,0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Anda", 1, (0, 0,255))
        win.blit(text, (180, 200))

        text = font.render("Lawan", 1, (255, 0, 0))
        win.blit(text, (380, 200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.bothWent():
            text1 = font.render(move1, 1, (255,255,255))
            text2 = font.render(move2, 1, (255,255,255))
        else:
            if game.p1Went and p == 0:
                text1 = font.render(move1, 1, (255,255,255))
            elif game.p1Went:
                text1 = font.render("Sudah Pilih", 1, (255,255,255))
            else:
                text1 = font.render("Menunggu..", 1, (255,255,255))

            if game.p2Went and p == 1:
                text2 = font.render(move2, 1, (255,255,255))
            elif game.p2Went:
                text2 = font.render("Sudah Pilih", 1, (255,255,255))
            else:
                text2 = font.render("Menunggu..", 1, (255,255,255))

        if p == 1:
            win.blit(text2, (100, 350))
            win.blit(text1, (380, 350))
        else:
            win.blit(text1, (100, 350))
            win.blit(text2, (380, 350))

        for btn in btns:
            btn.draw(win)

    pygame.display.update()
