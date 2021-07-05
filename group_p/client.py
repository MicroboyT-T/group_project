import pygame
from network import Network
import pickle
pygame.font.init()

width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

#Button interaction part#
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
        text = font.render(self.text, 1, (255,255,255))  #color set to white
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
    win.fill((0,0,0))   #set window background to black

    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 65)
        text = font.render("Menunggu Pemain Lain...", 1, (255,0,0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Anda", 1, (0, 0,255))      #color set to blue
        win.blit(text, (180, 200))

        text = font.render("Lawan", 1, (255, 0, 0))    #color set to red
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


#interface for winning and losing menu#

btns = [Button("Pistol", 50, 500, (44,53,57)), Button("Burung", 250, 500, (165,42,42)), Button("Air", 450, 500, (0,105,147))]   #color for "pistol" is gun metal, "Burung" is brown and "Air" is blue sea
def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("Anda Pemain", player)

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.bothWent():
            redrawWindow(win, game, player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            font = pygame.font.SysFont("comicsans", 90)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):  #interface to determine the winner#
                text = font.render("Anda Menang! :)", 1, (0,255,0))
            elif game.winner() == -1:
                text = font.render("Seri :|", 1, (255,215,0))
            else:
                text = font.render("Anda Kalah :(", 1, (255, 0, 0))

            win.blit(text, (width/2 - text.get_width()/2, (height/2 - text.get_height()/2) - 250))
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if not game.p1Went:
                                n.send(btn.text)
                        else:
                            if not game.p2Went:
                                n.send(btn.text)

        redrawWindow(win, game, player)  #prompt the winner#


#Menu screen#
def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((0,0,0))     #set menu background to black
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Tekan Untuk Mula!", 1, (255,0,0))  #set color to red
        win.blit(text, (100,200))  #size of font#
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

while True:
    menu_screen()
