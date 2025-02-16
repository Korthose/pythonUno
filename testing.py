import pygame

from Objects.Card import Card

import random

pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Basic Pygame program')

cards = []

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

randCards(cards)
print(cards)
