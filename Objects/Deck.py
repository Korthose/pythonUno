import random

import pygame

from Objects.Card import Card
from testing import randCards


class Deck:
    def __init__(self):

        self.red = 'Red'
        self.blue = 'Blue'
        self.yellow = 'Yellow'
        self.green = 'Green'

        self.deck = []
        self.playerCards = []
        self.cards = []

        self.startingCard = Card(random.randint(0, 9), random.choice(['Red', 'Blue', 'Yellow', 'Green']))

        self.screen = pygame.display.set_mode((1280, 720))
        self.screen.fill((159, 217, 255))


    def randColor(self):
        randColour = []

        randColour.extend([self.red] * 19)
        randColour.extend([self.blue] * 19)
        randColour.extend([self.yellow] * 19)
        randColour.extend([self.green] * 19)

        random.shuffle(randColour)
        return randColour

    def randInt(self):
        randNum = []

        randNum.extend([0] * 4)
        randNum.extend([1] * 8)
        randNum.extend([2] * 8)
        randNum.extend([3] * 8)
        randNum.extend([4] * 8)
        randNum.extend([5] * 8)
        randNum.extend([6] * 8)
        randNum.extend([7] * 8)
        randNum.extend([8] * 8)
        randNum.extend([9] * 8)

        random.shuffle(randNum)
        return randNum

    def createDeck(self):
        # need to be 92 after special cards

        colors = self.randColor()
        numbers = self.randInt()

        for i in range(76):
            # make card instance
            self.cards.append(Card(numbers[i], colors[i]))

        self.pullCards(7)
        print(self.cards)

    # used for initial player deck & pulling cards
    def pullCards(self, pulledCard):
        self.playerCards = self.cards[:pulledCard]
        del self.cards[:pulledCard]

    def starter(self):
        card_width = 180  # From your Card class
        start_x = (1280 - (len(self.playerCards) * card_width)) // 2
        start_y = 670 - card_width

        # card on table
        self.startingCard.moveTo((1280 - card_width) // 2, (720 - 180) // 2)
        self.startingCard.draw(self.screen)

        # playing card
        for i, card in enumerate(self.playerCards):
            x = start_x + i * card_width
            y = start_y
            card.moveTo(x, y)
            # startingCard.moveTo(x)
            card.draw(self.screen)

    # game starts
    # if not self.cardLength:
    #
    #     # # creating a starting card to place on
    #     # randomCombo = {
    #     #     'number': random.randint(1, 5),
    #     #     'color': random.choice(color)
    #     # }
    #     # startingCard = Card(randomCombo['number'], randomCombo['color'])
    #
    #     return True
    # # else:
    # #     randomCombo = {
    # #         'number': random.randint(1, 9),
    # #         'color': random.choice(color)
    # #     }
    # #
    # #     cards.append(Card(randomCombo['number'], randomCombo['color']))