import pygame
from functools import reduce

def cross(rect, x, y):
    X, Y = x * 100, y * 100
    pygame.draw.line(rect, (134, 52, 52), (X + 10, Y + 10), (X + 90, Y + 90), width=5)
    pygame.draw.line(rect, (141, 12, 24), (X + 90, Y + 10), (X + 10, Y + 90), width=5)

def circle(rect, x, y):
    X, Y = x * 100, y * 100
    pygame.draw.circle(rect, (150, 50, 50), (X + 50, Y + 50), 40, width=5)

class TicTacToe:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 300))
        pygame.display.set_caption("Tic Tac Toe")
        self.logo = pygame.image.load('logo.png')
        pygame.display.set_icon(self.logo)
        self.turn = True  
        self.running = True
        self.array = [[None for _ in range(3)] for _ in range(3)]
        self.winner = None

    def gameover(self):
        """Check if the game is over either by win or draw."""
        self.winner = self.check_win()
        if self.winner:
            print(f"Player '{self.winner}' wins!")
            return True
        elif all(all(cell is not None for cell in row) for row in self.array):
            print("It's a draw!")
            return True
        return False

    def check_win(self):
        """Check rows, columns, and diagonals for a win."""
        
        for i in range(3):
            if self.array[i][0] == self.array[i][1] == self.array[i][2] and self.array[i][0] is not None:
                return self.array[i][0]  # Row win
            if self.array[0][i] == self.array[1][i] == self.array[2][i] and self.array[0][i] is not None:
                return self.array[0][i] 

       
        if self.array[0][0] == self.array[1][1] == self.array[2][2] and self.array[0][0] is not None:
            return self.array[0][0]  
        if self.array[0][2] == self.array[1][1] == self.array[2][0] and self.array[0][2] is not None:
            return self.array[0][2] 

        return None 

    def gameloop(self):
        """Main game loop to handle events and drawing."""
        while self.running:
            self.screen.fill((255, 255, 255)) 

            # Draw grid lines
            pygame.draw.line(self.screen, (161, 27, 156), (0, 100), (300, 100), width=3)
            pygame.draw.line(self.screen, (161, 27, 156), (0, 200), (300, 200), width=3)
            pygame.draw.line(self.screen, (161, 27, 156), (100, 0), (100, 300), width=3)
            pygame.draw.line(self.screen, (161, 27, 156), (200, 0), (200, 300), width=3)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONUP and not self.gameover():
                    x, y = (i // 100 for i in pygame.mouse.get_pos())
                    if self.array[x][y] is None:  
                        if self.turn:
                            self.array[x][y] = '0'
                            cross(self.screen, x, y)
                        else:
                            self.array[x][y] = '+'
                            circle(self.screen, x, y)
                        self.turn = not self.turn  
                    else:
                        print("Invalid move, cell already filled.")

            
            for i in range(3):
                for j in range(3):
                    if self.array[i][j] == '0':
                        cross(self.screen, i, j)
                    elif self.array[i][j] == '+':
                        circle(self.screen, i, j)

            pygame.display.update()

if __name__ == '__main__':
    game = TicTacToe()
    game.gameloop()

