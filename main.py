import pygame
from functools import reduce,partial
def cross(rect,x,y):
    X,Y = x*100,y*100
    pygame.draw.line(rect,(134,52,52),(X+10,Y+10),(X+90,Y+90))
    pygame.draw.line(rect,(141,12,24),(X+90,Y+10),(X+10,Y+90))

def circle(rect,x,y):
    X,Y = x*100 ,y*100
    pygame.draw.circle(rect,(150,50,50),(X+50,Y+50),40,width = 1)

class TicTacToe:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((300,300))
        pygame.display.set_caption("Tic Tac Toe")
        self.logo = pygame.image.load('logo.png')
        pygame.display.set_icon(self.logo)
        self.turn = True
        self.running = True
        self.array = [[None for i in range(3)]for i in range(3)]
    def gameover(self):
        return False
    def gameloop(self):
        while self.running:
            if not self.gameover():
                pygame.draw.line(self.screen,(161, 27, 156),(0,100),(300,100))
                pygame.draw.line(self.screen,(161, 27, 156),(0,200),(300,200))
                pygame.draw.line(self.screen,(161, 27, 156),(100,0),(100,300))
                pygame.draw.line(self.screen,(161, 27, 156),(200,0),(200,300))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    elif event.type == pygame.MOUSEBUTTONUP:
                        x,y= (i//100 for i in pygame.mouse.get_pos())
                        if self.turn:
                            if not self.array[x][y]:
                                self.array[x][y] = "0"
                                cross(self.screen,x,y)
                                self.turn = not self.turn
                            else:
                                # you cannot draw
                                print("Invalid ")
                        else:
                            if not self.array[x][y]:
                                self.array[x][y] = "+"
                                circle(self.screen,x,y)
                                self.turn = not self.turn
                            else:
                                # you cannot draw
                                print("Invalid ")
                pygame.display.update()
    def check_win(self):
        diagonal = reduce(lambda x,y:)


if __name__ == '__main__':
    game = TicTacToe()
    game.gameloop()
