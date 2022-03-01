import pygame
pygame.init()
screen = pygame.display.set_mode((300,300))
pygame.display.set_caption("Tic Tac Toe")
logo = pygame.image.load('logo.png')

pygame.display.set_icon(logo)
turn = True
running = True
def cross(rect,x,y):
    x,y = x*100,y*100
    pygame.draw.line(screen,(134,52,52),(x*0.9,y*0.9),((x+100)*0.9,(y+100)*0.9))
    pygame.draw.line(screen,(141,12,24),((x+100)*0.9,y*0.9),(x*0.9,(y+100)*0.9))
def circle(rect,x,y):pass
while running:
    pygame.draw.line(screen,(161, 27, 156),(0,100),(300,100))
    pygame.draw.line(screen,(161, 27, 156),(0,200),(300,200))
    pygame.draw.line(screen,(161, 27, 156),(100,0),(100,300))
    pygame.draw.line(screen,(161, 27, 156),(200,0),(200,300))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            print("Button up")
    x,y= pygame.mouse.get_pos()
    #print(x//100,y//100)
    cross(screen,0,0)
    
      
    pygame.display.update()
