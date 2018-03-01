#shte trqbva da import tkinter, math (za button i za poziciqta na mishkata)
import os,pygame,math
import tkinter as tk
import random


white = [255, 255, 255]
black = [0, 0, 0]
green = [0, 240, 0]

width, height = 400, 400
bheight, bwidth = 80, 100


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def text_objects2(text, font):
    textSurface2 = font.render(text, True, black)
    return textSurface2, textSurface2.get_rect()


#display-a na koito se pokazva igrata, glavniq class(trqbva da sedi nai otgore)
class CardWar:

    def __init__(self):
        pass
        #1
        pygame.init()
        #2
        self.gameDisplay = pygame.display.set_mode((width, height))
        pygame.display.set_caption("CardWar")
        #3
        self.clock = pygame.time.Clock()
        #4
        self.gameDisplay.fill(white)
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects2("Click anywhere to start!", smallText)
        textRect.center = (height/2), (width/2)
        self.gameDisplay.blit(textSurf, textRect)

    def update(self):
        self.clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.gameDisplay.fill(black)
                pygame.display.update()
                pygame.draw.rect(self.gameDisplay, green, (50,50,80,50))
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects2("Yes!", smallText)
                textRect.center = (50+80/2), (50+50/2)
                self.gameDisplay.blit(textSurf, textRect)

        pygame.display.flip()


bg = CardWar()
while 1:
    bg.update()


from pygame.locals import *

from RandomCard import RandomCard
from Deck import Deck
from Player import Player
