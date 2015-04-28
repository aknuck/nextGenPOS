import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400,400))

xpos = 10
ypos = 20
xvel = 1
yvel = 1

green = pygame.Color(0,255,0)
black = pygame.Color(0,0,0)

while True:
    screen.fill(green)
    pygame.draw.circle(screen,black,(xpos,ypos),4)
    if xpos < 400 and xpos > 0:
        xpos += xvel
    else:
        xvel = -xvel
        xpos += xvel
    if ypos < 400 and ypos > 0:
        ypos += yvel
    else:
        yvel = -yvel
        ypos += yvel
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()