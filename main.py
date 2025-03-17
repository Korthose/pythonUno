import random
import pygame
from socket import *
from pygame.locals import *
from Objects.Card import Card
from Objects.Deck import Deck

#variables
cards = []
Deck = Deck()

# Initialise screen
pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Python')

# Fill background
screen.fill((159, 217, 255))

# Initial deck creation
Deck.createDeck()
Deck.starter()

#Event loop
while True:
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and pygame.Rect.collidepoint(Deck.stackRect, mouse):
                Deck.pullCards(1)
                Deck.redraw()
                break

            for playerCard in list(Deck.playerCards):
                if playerCard.playing(event, Deck.initialCard, mouse):
                    # remove the played card & generate new starter card
                    screen.fill((159, 217, 255))
                    Deck.cardPlayed(playerCard)
                    break
            # if event.button == 1 and pygame.Rect.collidepoint(, mouse):

    # for playerCard in list(Deck.playerCards):
    #     if playerCard.rect.collidepoint(mouse):
    #         playerCard.rect.y -= 20
    #         playerCard.draw(screen)

    pygame.display.update()
