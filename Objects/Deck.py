import random

import pygame

from Objects.Card import Card
from testing import randCards


class Deck:
    def __init__(self):
        self.card_width = 180
        self.card_height = 180

        self.red = 'Red'
        self.blue = 'Blue'
        self.yellow = 'Yellow'
        self.green = 'Green'

        self.playerCards = []
        self.cards = []

        self.cardStack = pygame.image.load("Resources/Sprites/Cards/Special/card_back.png").convert_alpha()
        self.cardStack = pygame.transform.scale(self.cardStack, (180, 180))
        self.stackRect = self.cardStack.get_rect()

        self.initialCard = Card(random.randint(0, 9), random.choice(['Red', 'Blue', 'Yellow', 'Green']))

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

        self.stackedCards()

        for i in range(76):
            # make card instance
            self.cards.append(Card(numbers[i], colors[i]))

        self.pullCards(7)

    # used for initial player deck & pulling cards
    def pullCards(self, pulledCard):
        if not self.playerCards:
            self.playerCards.extend(self.cards[:pulledCard])
        else:
            self.playerCards = self.cards[:pulledCard]

        del self.cards[:pulledCard]

    def stackedCards(self):
        self.stackRect.topleft = (((1280 - 180) // 2) + 160, (720 - 180) // 2)
        self.screen.blit(self.cardStack, self.stackRect)

    def redraw(self):
        self.starter()

        self.stackedCards()

        pygame.display.flip()

    def cardPlayed(self, matchedCard):
        # remove played card
        self.playerCards.remove(matchedCard)

        # declare played card as next card on table
        self.initialCard = matchedCard

        self.redraw()

    def starter(self):
        start_x = (1280 - (len(self.playerCards) * self.card_width)) // 2
        start_y = 670 - self.card_width

        # card on table
        self.initialCard.moveTo(((1280 - self.card_width) // 2) - 180, (720 - 180) // 2)
        self.initialCard.draw(self.screen)

        # playing card
        for i, card in enumerate(self.playerCards):
            x = start_x + i * self.card_width
            y = start_y
            card.moveTo(x, y)
            # startingCard.moveTo(x)
            card.draw(self.screen)

        print(self.playerCards)