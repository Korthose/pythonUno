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

Deck.createDeck()

#Event loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        # elif event.type == MOUSEBUTTONDOWN:
        #     for card in list(cards):  # Use list(cards) to create a copy
        #         if card.playCard(event, startingCard):
        #             # remove the played card
        #             cards.remove(card)
        #
        #             # generate new starting card
        #             randomCombo = {
        #                 'number': random.randint(1, 5),
        #                 'color': random.choice(color)
        #             }
        #             startingCard = Card(randomCombo['number'], randomCombo['color'])
        #             break  # Important: Exit the inner loop after removing a card
    Deck.starter()

    pygame.display.flip()
