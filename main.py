import random
import pygame
from socket import *
from pygame.locals import *
from Objects.Card import Card


cards = []

# Initialise screen
pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Basic Pygame program')

# Fill background
screen.fill((250, 250, 250))

def randCards(cards):
    color = ['Red', 'Blue', 'Yellow', 'Green']
    # game starts
    if not cards:
        for i in range(8):
            randomCombo = {
                'number': random.randint(1, 9),
                'color': random.choice(color)
            }

            cards.append(Card(randomCombo['number'], randomCombo['color']))
        return True

    else:
        randomCombo = {
            'number': random.randint(1, 9),
            'color': random.choice(color)
        }

        cards.append(Card(randomCombo['number'], randomCombo['color']))

# Event loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    randCards(cards)
    for i, card in enumerate(cards):
        card.moveTo(250, 50 + (i * 32//4) )
        card.draw(screen)
    pygame.display.flip()
