import os, pygame, math
import tkinter as tk
import random
from Deck import Deck

white = [255, 255, 255]
black = [0, 0, 0]
green = [0, 200, 0]

width, height = 400, 400
bheight, bwidth = 80, 100


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def text_objects2(text, font):
    textSurface2 = font.render(text, True, black)
    return textSurface2, textSurface2.get_rect()


class CardWar:

    def __init__(self):
        pass

        pygame.init()

        self.gameDisplay = pygame.display.set_mode((width, height))
        pygame.display.set_caption("CardWar")

        self.clock = pygame.time.Clock()


        self.gameDisplay.fill(black)
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("Click anywhere to start!", smallText)
        textRect.center = (height/2), (width/2)
        self.gameDisplay.blit(textSurf, textRect)

    def update(self):
        self.clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                exit()

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            import time
            game_start = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.gameDisplay.fill(white)
                pygame.draw.rect(self.gameDisplay, green, (100, 150, 200, 50))
                smallText = pygame.font.Font("freesansbold.ttf", 20)
                textSurf, textRect = text_objects2("Start Game", smallText)
                textRect.center = (100+200/2), (150+50/2)
                self.gameDisplay.blit(textSurf, textRect)
                smallText = pygame.font.Font("freesansbold.ttf", 40)
                textSurf, textRect = text_objects2("Card Wars", smallText)
                textRect.center = (width/2), (height-350)
                self.gameDisplay.blit(textSurf, textRect)
                pygame.display.update()

            background = pygame.image.load("belote.png")

            if 100+200 > mouse[0] > 100 and 150+50 > mouse[1] > 150:
                if click[0] == 1:
                    game_start = True
                        
            while game_start == True:
                self.gameDisplay.fill(black)
                self.gameDisplay.blit(background, (0, 0))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    self.gameDisplay.fill(black)
                    smallText = pygame.font.Font("freesansbold.ttf", 30)
                    textSurf, textRect = text_objects("Game Over", smallText)
                    textRect.center = (width / 2), ((height / 2)-10)
                    self.gameDisplay.blit(textSurf, textRect)
                    smallText = pygame.font.Font("freesansbold.ttf", 15)
                    textSurf, textRect = text_objects("(Click to go back)", smallText)
                    textRect.center = (width / 2), ((height / 2)+20)
                    self.gameDisplay.blit(textSurf, textRect)
                    pygame.display.update()
                    game_start = False

        pygame.display.flip()


bg = CardWar()
while 1:
    bg.update()
