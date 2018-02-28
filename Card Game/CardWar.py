#shte trqbva da import tkinter, math (za button i za poziciqta na mishkata)
import os,pygame,math
import tkinter as tk
import random


white = [255,255,255]
black = [0,0,0]

bheight, bwidth = 80, 100


def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

#display-a na koito se pokazva igrata, glavniq class(trqbva da sedi nai otgore)
class CardWar():		
    def __init__(self):
        pass
        #1
        pygame.init()
        width, height = 400, 400
        #2
        self.gameDisplay = pygame.display.set_mode((width, height))
        pygame.display.set_caption("CardWar")
        #3
        self.clock=pygame.time.Clock()        
               
    def update(self):
        self.clock.tick(60)

        self.gameDisplay.fill(white)
        pygame.draw.rect(self.gameDisplay, (0,230,0), (bwidth,40,bheight,40))
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("GO!", smallText)
        textRect.center = ( (bwidth+(bheight/2)), (40+(40/2)) )
        self.gameDisplay.blit(textSurf, textRect)
        
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


        pygame.display.flip()

bg=CardWar()
while 1:
    bg.update()


from pygame.locals import *

from RandomCard import RandomCard
from Deck import Deck
from Player import Player
